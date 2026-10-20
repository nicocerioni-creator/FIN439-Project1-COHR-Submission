"""Lab07: COHR reported annual P/E comparison as of September 15, 2026.

Execution authorized by the user; retain excluded candidates for diagnostics.
Prices: September 15, 2026 regular-session closes, USD per listed share.
EPS: latest full-year GAAP diluted EPS public by that date; no adjusted EPS.
Sources, periods, exclusions and unresolved checks: COHR_Lab07_Sources_2026-09-15.md.
"""

# Numeric strings preserve input decimals; None means missing.
VALUATION_DATE = "2026-09-15"
TARGET = {"ticker": "COHR", "name": "Coherent Corp.",
          "price": "271.17", "eps": "4.12",
          "fiscal_year_end": "2026-06-30", "publication_date": "2026-08-12"}
PEERS = [
    {"ticker": "FN", "name": "Fabrinet", "price": "374.91", "eps": "13.05",
     "fiscal_year_end": "2026-06-26", "publication_date": "2026-08-17",
     "policy": "Qualify: optical manufacturing and datacenter/communications demand; "
               "contract-manufacturing economics differ from COHR. "
               "Exact comparison-date market-cap verification remains unresolved."},
    {"ticker": "LITE", "name": "Lumentum Holdings Inc.",
     "price": "838.96", "eps": "-92.96",
     "fiscal_year_end": "2026-06-27", "publication_date": "2026-08-11",
     "policy": "Qualify as business candidate: optical products, AI/network demand, "
               "and manufacturing investment. Exclude from reported P/E: negative annual EPS.",
     "eps_source": "FY2026 SEC 10-K, Item 8, Note 3, Earnings Per Share, p. 83"},
]
# LITE is included for diagnostics only; pe() rejects its negative EPS.
# It cannot enter the usable peer multiples, median, or implied valuation.

from fractions import Fraction
from statistics import median


def positive_number(value):
    """Return an exact rational number, or None for unusable inputs."""
    if isinstance(value, bool):
        return None
    try:
        number = Fraction(str(value))
    except (ValueError, TypeError, ZeroDivisionError):
        return None
    return number if number > 0 else None


def ticker(company):
    return str(company.get("ticker") or "").strip().upper()


def pe(company):
    price = positive_number(company.get("price"))
    eps = positive_number(company.get("eps"))
    return price / eps if price is not None and eps is not None else None


def formatted(value, digits=2, signed=False):
    """Round only for display, using exact integer arithmetic (half-even)."""
    scale = 10 ** digits
    whole, remainder = divmod(abs(value.numerator) * scale, value.denominator)
    if remainder * 2 > value.denominator or (
        remainder * 2 == value.denominator and whole % 2
    ):
        whole += 1
    prefix = "-" if value < 0 else ("+" if signed else "")
    return f"{prefix}{whole // scale:,}.{whole % scale:0{digits}d}"


def main(target=None, peers=None):
    target = TARGET if target is None else target
    peers = PEERS if peers is None else peers
    print(f"ComparablePolicy | {VALUATION_DATE} | Lab07")
    print("September 15, 2026 closing prices; latest full-year GAAP diluted EPS")
    print("public by that date. USD per listed share; no adjusted or quarterly EPS.")
    print("P/E is equity-to-equity: no cash/debt bridge.\n")

    print("Input audit (USD per share):")
    for company in [target, *peers]:
        print(f"  {ticker(company)}: price=${company.get('price')}; "
              f"annual reported diluted EPS=${company.get('eps')}; "
              f"FY end={company.get('fiscal_year_end', 'unresolved')}; "
              f"published={company.get('publication_date', 'unresolved')}")
    print()

    # Deduplicate by normalized ticker; the first occurrence wins.
    unique = []
    seen = set()
    for company in peers:
        symbol = ticker(company)
        if not symbol:
            print("Excluded peer without a ticker: cannot identify/deduplicate.")
        elif symbol == ticker(target):
            print(f"Excluded target from peers: {symbol}")
        elif symbol in seen:
            print(f"Removed duplicate peer: {symbol} (first occurrence retained)")
        else:
            seen.add(symbol)
            unique.append(company)

    target_eps = positive_number(target.get("eps"))
    target_pe = pe(target)
    print(f"Target: {ticker(target)} — {target.get('name', '')}")
    print("Target P/E: " + (formatted(target_pe, 6) + "x" if target_pe is not None
                              else "not meaningful (missing, invalid, or nonpositive price/EPS)"))
    if target_eps is None:
        print("All implied target prices: not meaningful (invalid target EPS).")
    print()

    valid = {}
    for company in unique:
        symbol = ticker(company)
        multiple = pe(company)
        print(f"{symbol}: {company.get('policy', 'Candidate peer')}")
        if multiple is None:
            if company.get("eps_source"):
                print(f"  EPS source: {company['eps_source']}")
            print("  P/E and peer-implied price: not meaningful "
                  "(missing, invalid, or nonpositive price/EPS).")
        else:
            valid[symbol] = multiple
            implied = ("$" + formatted(multiple * target_eps)
                       if target_eps is not None else "not meaningful")
            print(f"  P/E: {formatted(multiple, 6)}x; implied target price: {implied}")

    print(f"\nUnique peers with usable positive P/E inputs: {len(valid)}")
    full_estimate = None
    if not valid:
        print("No usable peers. No estimate.")
    else:
        multiples = list(valid.values())
        midpoint = median(multiples)
        print(f"Median peer P/E: {formatted(midpoint, 6)}x")
        if target_eps is not None:
            full_estimate = midpoint * target_eps
        if len(valid) == 1:
            estimate = ("$" + formatted(full_estimate)
                        if full_estimate is not None else "not meaningful")
            print(f"One valid peer: reference estimate {estimate}; no range.")
        else:
            for label, multiple in (("Minimum", min(multiples)),
                                    ("Median", midpoint),
                                    ("Maximum", max(multiples))):
                implied = ("$" + formatted(multiple * target_eps)
                           if target_eps is not None else "not meaningful")
                print(f"{label}: {formatted(multiple, 6)}x -> {implied}")

    baseline_label = ("single-peer reference" if len(valid) == 1 else
                      "two-peer midpoint" if len(valid) == 2 else "full-peer median estimate")
    print(f"\nPeer-removal sensitivity (change from {baseline_label}):")
    if full_estimate is not None:
        print(f"Baseline {baseline_label}: ${formatted(full_estimate)}")
    if not unique:
        print("No peers to remove.")
    for company in unique:
        symbol = ticker(company)
        remaining_symbols = [key for key in valid if key != symbol]
        remaining = [value for key, value in valid.items() if key != symbol]
        if not remaining:
            print(f"Remove {symbol}: no usable peers remain; no estimate or dollar change.")
        elif target_eps is None:
            print(f"Remove {symbol}: implied price and dollar change not meaningful "
                  "(invalid target EPS).")
        else:
            estimate = median(remaining) * target_eps
            change = estimate - full_estimate
            note = "; one-peer reference, no range" if len(remaining) == 1 else ""
            sign = "-" if change < 0 else "+"
            print(f"Remove {symbol}: {target.get('name', ticker(target))} "
                  f"({ticker(target)}) target + {', '.join(remaining_symbols)} peer(s) remain.")
            print(f"  Remaining median P/E: {formatted(median(remaining), 6)}x")
            print(f"  Implied target price: ${formatted(estimate)}{note}")
            print(f"  Change from {baseline_label}: {sign}${formatted(abs(change))} "
                  "(calculated before rounding)")


if __name__ == "__main__":
    main()
