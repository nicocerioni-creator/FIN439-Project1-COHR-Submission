"""Local, dependency-free driver workbench. python3 project1/app.py"""
import argparse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
from engine import run, full_report, DRIVERS, ROOT

PAGE = r'''<!doctype html><html lang="en"><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>COHR | Project 1 FCFF Workbench</title>
<style>
*{box-sizing:border-box}body{font:15px/1.45 system-ui,sans-serif;background:#f3f5f8;color:#172433;margin:0}header{background:#183348;color:white;padding:20px 30px}h1{font-size:25px;margin:0}h2{font-size:19px;margin:22px 0 10px}h3{font-size:16px}main{padding:20px 28px;max-width:1600px;margin:auto}.layout{display:grid;grid-template-columns:310px 1fr;gap:22px}aside,.card{background:white;border:1px solid #d9e0e5;border-radius:8px;padding:16px;margin-bottom:14px}.muted{color:#596978;font-size:13px}.warning{background:#fff3d7;padding:12px;border-left:5px solid #d39a19;margin:12px 0}.pass{background:#e0f3e9;color:#155e3d;padding:12px}.fail{background:#ffe1e1;color:#9a2020;padding:12px}button{background:#194c70;color:white;border:0;border-radius:4px;padding:9px 12px;cursor:pointer;margin:3px 2px}button.secondary{background:#566675}label{display:block;margin:16px 0 4px;font-weight:600}input{width:100%}.metrics{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}.metric{background:white;padding:15px;border:1px solid #d9e0e5;border-radius:6px}.big{font-size:26px;font-weight:650}.scroll{overflow:auto}table{width:100%;border-collapse:collapse;font-size:13px}th,td{text-align:right;padding:7px;border-bottom:1px solid #e0e5ea;white-space:nowrap}th:first-child,td:first-child{text-align:left}th{background:#edf2f6}details{margin:12px 0}summary{cursor:pointer;font-weight:600}.bad{color:#a02020;font-weight:650}a{color:#15577c}#error{color:#a02020}@media(max-width:1000px){.layout{grid-template-columns:1fr}.metrics{grid-template-columns:1fr}}
.layout{grid-template-columns:260px minmax(0,1fr)}.layout>section,.layout>aside{min-width:0}.scroll{max-width:100%}@media(max-width:1000px){.layout{grid-template-columns:225px minmax(0,1fr);gap:12px}main{padding:14px}.metrics{grid-template-columns:1fr}.metric{padding:9px}.big{font-size:22px}header{padding:16px}h1{font-size:22px}aside{padding:12px}}@media(max-width:640px){.layout{grid-template-columns:1fr}}
header{padding:13px 24px}header h1{font-size:23px}.decision{background:white;padding:13px 16px;margin-bottom:14px;border-left:5px solid #194c70}.decision strong{font-size:19px}label{margin-top:10px}aside{align-self:start}aside h2{margin-bottom:7px}.assumption-flag{color:#9a2020;font-weight:600}.summary-line{margin:10px 0;color:#43576a}.button-row{position:sticky;top:0;background:white;padding:6px 0;z-index:1}.scenario-note{font-size:13px}.risk-list{margin-bottom:8px}
input[type=number]{width:78px;padding:4px;border:1px solid #afbbc5;border-radius:3px;font:inherit}.exact-row{display:flex;align-items:center;justify-content:space-between;gap:6px}.number-label{font-size:12px;font-weight:400;margin:0}
</style>
<header><h1>COHR · Corporate Finance Workbench</h1><div>Buy-side investment committee · No current position · Valuation / information cutoff: September 15, 2026</div></header>
<main><div class="decision"><strong>Committee action: watch / defer</strong><div id="range"></div><div class="muted">3–5 year decision horizon · USD · Actual common shares · Conditional scenarios, not a confidence interval</div><details><summary>Why the fund should wait</summary><ul class="risk-list"><li>Capacity investment may not pay off if AI-infrastructure demand slows.</li><li>FY2026 CFO was $79.514m; CFO less PP&E capex was negative $1,023.395m.</li><li>Two customers supplied 32% of sales. Datacenter & Communications supplied 74.1%, including non-AI applications; customer leverage and pricing pressure are risks.</li></ul><p class="muted">Revisit after two reporting dates of improving trailing-year CFO less PP&E capex, supported capacity utilization, a reconciled funding plan and valuation with a 25% margin of safety.</p></details></div>
<div class="layout"><aside><h2 style="margin-top:0">Bounded driver panel</h2><div class="muted">Shifts apply to every forecast year. Accounting, source data and checks are locked.</div>
<div class="button-row"><button id="reset">Restore base</button><button id="stress" class="secondary">Growth funding stress</button></div><div id="controls"></div><p id="error" role="alert"></p>
<details><summary>How to use</summary><p>Change one driver, read the change from restored base, follow EBIT → reinvestment → FCFF → value, and inspect all failed checks. Restore base before another comparison.</p><p>The stress button uses a permitted growth input that breaches financing capacity. It does not tamper with accounting.</p></details></aside>
<section><div class="metrics"><div class="metric"><div>Conditional FCFF value / share</div><div class="big" id="price"></div><div id="delta"></div></div><div class="metric"><div>FY2031 operating profit / EBIT</div><div class="big" id="ebit"></div><div class="muted" id="ebitdelta"></div></div><div class="metric"><div>FY2031 signed FCFF</div><div class="big" id="fcff"></div><div class="muted" id="fcffdelta"></div></div></div><div class="summary-line">September 15 market reference: <b>$271.17</b> · Terminal PV / EV: <b id="terminal"></b></div>
<h2>Checks that can fail</h2><div id="checks" aria-live="polite"></div>
<details><summary>All reconciliation checks</summary><div class="scroll" id="checktable"></div></details>
<details><summary class="assumption-flag">Historical-band departures — deliberate assumptions to challenge</summary><div class="scroll" id="history"></div><p class="muted">Red history flags identify forecasts outside FY2024–FY2026 observations. They require the recorded business rationale; they are separate from accounting and funding validity. Reset restores the original forward assumptions, not a claim that the future equals history.</p></details>
<h2>Causal low / base / high cases</h2><div class="card scroll" id="scenarios"></div><p class="muted">These are analyst scenarios, not probabilities. The failed sticky-investment stress is preserved and excluded from the passing-case range.</p>
<h2>Five-year statements and operating cash flow</h2><div class="muted">USD millions. Full fiscal years; the DCF separately uses a remaining-FY2027 stub from September 15. D&A is already included in GAAP operating expenses.</div><div class="card scroll" id="statements"></div>
<h2>Enterprise → common equity → per share</h2><div class="card" id="bridge"></div>
<h2>Market-implied expectation</h2><div class="card" id="reverse"></div>
<h2>One-at-a-time sensitivity against the same base</h2><div class="muted">Full and half ranges test range dependence. Values for funding-invalid endpoints are conditional operating diagnostics, excluded from any executable valuation range.</div><div class="card scroll" id="sens"></div>
<details><summary>Which drivers carry EBIT, FCFF and value?</summary><div id="ranking"></div></details>
<h2>WACC–growth sensitivity</h2><div class="card scroll" id="grid"></div>
<h2>Comparable-company cross-checks</h2><div class="card scroll" id="peers"></div>
<h2>WACC build and terminal challenge</h2><div class="card scroll" id="wacc"></div><div class="card scroll" id="terminalstress"></div>
<details open><summary>Assumptions, dates and limitations</summary><div id="limitations"></div><div class="scroll" id="assumptions"></div></details>
<p class="muted">Working sources: docs/project-1-audit.md; docs/validation-and-ai-use.md. Original lab files are preserved. This draft is not the completed submission.</p></section></div></main>
<script>
const initial=__REPORT__, schema=__SCHEMA__;let base=initial,sequence=0;
const names={growth_shift_pp:'Revenue growth shift',margin_shift_pp:'Gross margin shift',capex_shift_pp:'PP&E capex / revenue shift',inventory_shift_days:'Ending inventory days shift',wacc_pct:'WACC',terminal_growth_pct:'Terminal growth'};
const fmt=x=>Number(x).toLocaleString('en-US',{minimumFractionDigits:2,maximumFractionDigits:2});const money=x=>'$'+fmt(x);
const esc=x=>String(x).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;');
const table=(heads,rows)=>'<table><thead><tr>'+heads.map(h=>'<th>'+esc(h)+'</th>').join('')+'</tr></thead><tbody>'+rows.map(row=>'<tr>'+row.map(v=>'<td>'+esc(v)+'</td>').join('')+'</tr>').join('')+'</tbody></table>';
document.getElementById('range').textContent='Passing-case DCF range '+money(initial.passing_scenario_range[0])+'–'+money(initial.passing_scenario_range[1])+'/share versus $271.17 market reference. Base WACC 11.8%; terminal growth 3%.';
for(const [k,d]of Object.entries(schema)){
 document.getElementById('controls').insertAdjacentHTML('beforeend',`<label for="${k}">${names[k]} <output id="${k}_out">${d.base} ${d.unit}</output></label><input type="range" id="${k}" min="${d.min}" max="${d.max}" step="${d.step}" value="${d.base}"><div class="exact-row"><span class="muted">${d.min} to ${d.max} ${d.unit}</span><label class="number-label" for="${k}_exact">Exact <input type="number" aria-label="${names[k]} exact value" id="${k}_exact" min="${d.min}" max="${d.max}" step="${d.step}" value="${d.base}"></label></div>`);
 document.getElementById(k).addEventListener('input',()=>{document.getElementById(k+'_out').textContent=document.getElementById(k).value+' '+d.unit;document.getElementById(k+'_exact').value=document.getElementById(k).value;update()});
 document.getElementById(k+'_exact').addEventListener('change',()=>{const raw=document.getElementById(k+'_exact').value;const value=Number(raw);const steps=(value-d.min)/d.step;if(raw.trim()===''||!Number.isFinite(value)||value<d.min||value>d.max||Math.abs(steps-Math.round(steps))>1e-7){document.getElementById('error').textContent=names[k]+' must be between '+d.min+' and '+d.max+' '+d.unit+' in increments of '+d.step+'. Input not applied.';return}document.getElementById(k).value=value;document.getElementById(k+'_out').textContent=value+' '+d.unit;update()});
}
function draw(r){const v=r.valuation;document.getElementById('price').textContent=money(v.per_share);document.getElementById('delta').textContent=money(v.per_share-base.valuation.per_share)+' vs restored base'+(!r.all_checks_pass?' · FUNDING INVALID':'');document.getElementById('terminal').textContent=fmt(v.terminal_share*100)+'%';
const last=r.statements.at(-1),baseLast=base.statements.at(-1);for(const[id,key]of [['ebit','operating_income'],['fcff','fcff']]){document.getElementById(id).textContent=money(last[key])+'m';document.getElementById(id+'delta').textContent=money(last[key]-baseLast[key])+'m vs base'}
document.getElementById('history').innerHTML=table(['Driver','FY2024–26 historical band','Forecast years outside','Status'],r.historical_band_checks.map(h=>[h.driver,fmt(h.historical_min*100)+'%–'+fmt(h.historical_max*100)+'%',h.outside_years.join(', '),h.within_history?'WITHIN':'OUTSIDE — judgment required']));
const failed=r.checks.filter(x=>!x.pass);document.getElementById('checks').className=failed.length?'fail':'pass';document.getElementById('checks').innerHTML=failed.length?'<b>FAIL — funding or reconciliation condition breached.</b><br>'+failed.map(x=>esc(x.check)+': '+fmt(x.gap)+' '+esc(x.unit)).join('<br>'):'PASS — base-year balance-sheet checks, annual articulation, funding and equity bridge pass.';
document.getElementById('checktable').innerHTML=table(['Check','Status','Gap ($m)'],r.checks.map(x=>[x.check,x.pass?'PASS':'FAIL',fmt(x.gap)]));
const fields=[['Income statement',''],['Revenue','revenue'],['COGS','cost_of_sales'],['Gross profit','gross_profit'],['SG&A','sga'],['R&D','rd'],['EBIT','operating_income'],['Interest incl. debt costs','interest'],['Tax','tax'],['Net income','net_income'],['Balance sheet',''],['Cash','cash'],['Short-term investments','short_term_investments'],['Restricted cash','restricted_cash'],['Inventory','inventory'],['PP&E net','ppe'],['Intangibles net','intangibles'],['Other operating assets','other_operating_assets'],['Other assets','other_assets'],['Total assets','assets'],['Debt carrying value','debt'],['Revolver','revolver'],['Operating liabilities','operating_liabilities'],['Other liabilities','other_liabilities'],['Parent equity','equity'],['NCI','nci'],['Liabilities and equity','liabilities_equity'],['Cash flow / FCFF',''],['Depreciation','depreciation'],['Amortization','amortization'],['Inventory investment','change_inventory'],['Other WC investment','change_other_wc'],['Operating cash flow','operating_cash_flow'],['PP&E capex','capex'],['Intangible purchases','intangible_purchases'],['Investing cash flow','investing_cash_flow'],['Financing cash flow','financing_cash_flow'],['Cash change','change_cash'],['Signed FCFF','fcff']];
document.getElementById('statements').innerHTML=table(['USD millions',...r.statements.map(x=>'FY'+x.year)],fields.map(([label,k])=>[label,...r.statements.map(x=>k?fmt(x[k]):'')]));
const b=r.bridge;document.getElementById('bridge').innerHTML=table(['Bridge item','$ millions'],[['Enterprise value',fmt(v.enterprise_value)],['+ Unrestricted cash',fmt(b.cash)],['− Retained operating cash',fmt(b.operating_cash_retained)],['+ Short-term investments',fmt(b.short_term_investments)],['− Gross debt',fmt(b.gross_debt)],['− Finance leases',fmt(b.finance_leases)],['− Pension deficit',fmt(b.pension_deficit)],['− NCI proxy',fmt(b.nci)],['− Preferred',fmt(b.preferred)],['Common equity value',fmt(v.equity_value)],['Actual common shares (million)',fmt(r.shares_million)],['Value / share',money(v.per_share)]])+'<p class="muted">Restricted cash is excluded. Debt principal, pension deficits and NCI book value proxy market claims. Operating lease costs remain in operating cash flows. June 30 balances and August 10 common shares proxy September 15 amounts.</p>';
const rev=v.reverse_dcf;document.getElementById('reverse').textContent='Holding explicit FCFF, WACC, terminal growth and the bridge fixed, the market reference requires terminal FCFF of '+money(rev.required_terminal_fcff)+' million, or '+fmt(rev.multiple_of_base_terminal_fcff)+'× this scenario’s terminal FCFF. This is an implied condition, not a prediction.';
document.getElementById('limitations').innerHTML='<ul>'+r.limitations.map(x=>'<li>'+esc(x)+'</li>').join('')+'</ul>';document.getElementById('assumptions').innerHTML=table(['Locked/base assumption','Value'],Object.entries(r.assumptions).map(([k,v])=>[k,Array.isArray(v)?v.map(x=>Number(x).toFixed(4)).join(' / '):String(v)]));}
document.getElementById('scenarios').innerHTML=table(['Scenario','Value / share','Checks'],initial.scenarios.map(s=>[s.name,money(s.per_share),s.valid?'PASS':'FAIL — excluded']))+'<details class="scenario-note"><summary>Causal assumptions behind the cases</summary>'+initial.scenarios.map(s=>'<p><b>'+esc(s.name)+':</b> '+esc(s.cause)+'</p>').join('')+'</details>';
const p=initial.peers;document.getElementById('peers').innerHTML=table(['Company','Market cap $m','EV / sales','EV / EBITDA','Reported P/E'],Object.entries(p.rows).map(([k,x])=>[k,fmt(x.market_cap),fmt(x.ev_sales),fmt(x.ev_ebitda),fmt(x.pe)]))+table(['FN-based COHR reference','USD / share'],Object.entries(p.single_peer_references_per_share).map(([k,v])=>[k,money(v)]))+'<p>'+esc(p.policy_check)+'</p><p>'+esc(p.cash_policy)+'</p><ul>'+p.limitations.map(x=>'<li>'+esc(x)+'</li>').join('')+'</ul>';
const wb=initial.wacc_build;document.getElementById('wacc').innerHTML=table(['Component','Value / basis'],[['Risk-free nominal 10-year','5.00%, September 15 Treasury'],['ERP','4.14%, September 1 Damodaran estimate'],['Beta','1.75 analyst judgment; NOT a regression'],['Cost of equity',fmt(wb.cost_of_equity*100)+'%'],['Pretax debt cost','5.5% judgment, historical proxy'],['Tax shield rate','20% normalized judgment'],['Equity / debt weights',fmt(wb.equity_weight*100)+'% / '+fmt(wb.debt_weight*100)+'%'],['Calculated / rounded WACC',fmt(wb.calculated_wacc*100)+'% / '+schema.wacc_pct.base+'%']])+'<p>'+esc(wb.classification)+'</p>';
document.getElementById('terminalstress').innerHTML='<b>Alternative terminal return assumptions, same base forecast and WACC</b>'+table(['Terminal return on new capital','Terminal FCFF $m','Value / share'],initial.terminal_roic_stress.map(s=>[fmt(s.roic*100)+'%',fmt(s.terminal_fcff),money(s.per_share)]))+'<p class="muted">Alternative terminal reinvestment = terminal NOPAT × g / return on new capital. These are assumption challenges, not additional probabilities or an averaged value.</p>';
document.getElementById('sens').innerHTML=table(['Driver','Range scale','Low input','High input','Low $/share','High $/share','Conditional span','Low checks','High checks'],initial.sensitivity.map(s=>[names[s.driver],s.range_scale,s.low_input,s.high_input,fmt(s.low_value),fmt(s.high_value),fmt(s.conditional_value_span),s.low_valid?'PASS':'FAIL',s.high_valid?'PASS':'FAIL']));
document.getElementById('ranking').innerHTML='<p>Among passing endpoints plus the same base, revenue growth drives FY2031 EBIT most; PP&E capex intensity drives FY2031 FCFF most; WACC drives value most. These are range-specific comparisons. At half ranges, inventory days overtakes growth for FCFF; the other leading drivers remain the same. FCFF excludes borrowing, so this ranking need not match the old FCFE lab.</p>'+table(['Driver','Range scale','Valid EBIT span $m','Valid FCFF span $m','Valid value span $/share','Valid endpoints'],initial.sensitivity_valid_spans.map(s=>[names[s.driver],s.range_scale,fmt(s.ebit_valid_span),fmt(s.fcff_valid_span),fmt(s.value_valid_span),s.valid_endpoints.join(', ')]))+'<p class="muted">WACC and terminal growth affect valuation only. Capex and inventory sensitivities hold operating margins fixed, so their direct EBIT effect is zero in this controlled exercise. Read the input ranges and asymmetric exclusions before comparing spans.</p>';
document.getElementById('grid').innerHTML=table(['WACC / terminal g','2%','3%','4%'],[9,10,11,11.8,12,13].map(w=>[w+'%',...[2,3,4].map(g=>money(initial.wacc_growth_grid.find(x=>x.wacc_pct===w&&x.g_pct===g).per_share))]));
async function update(){const my=++sequence;const controls=Object.fromEntries(Object.keys(schema).map(k=>[k,Number(document.getElementById(k).value)]));try{const response=await fetch('/api/run',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(controls)});const r=await response.json();if(my!==sequence)return;if(!response.ok)throw Error(r.error);document.getElementById('error').textContent='';draw(r)}catch(e){if(my===sequence)document.getElementById('error').textContent='Live calculation unavailable. Run python3 project1/app.py and open the local URL. '+e.message}}
function reset(){for(const[k,d]of Object.entries(schema)){document.getElementById(k).value=d.base;document.getElementById(k+'_exact').value=d.base;document.getElementById(k+'_out').textContent=d.base+' '+d.unit}sequence++;document.getElementById('error').textContent='';draw(base)}
document.getElementById('reset').onclick=reset;document.getElementById('stress').onclick=()=>{reset();document.getElementById('growth_shift_pp').value=5;document.getElementById('growth_shift_pp_exact').value=5;document.getElementById('growth_shift_pp_out').textContent='5 pp';update()};draw(initial);
</script></html>'''


def report():
    return full_report()


def html_page():
    return PAGE.replace('__REPORT__',json.dumps(report(),allow_nan=False)).replace('__SCHEMA__',json.dumps(DRIVERS)).encode()


class Handler(BaseHTTPRequestHandler):
    def send(self, code, content, kind):
        self.send_response(code)
        self.send_header('Content-Type',kind)
        self.send_header('Content-Length',str(len(content)))
        self.send_header('Cache-Control','no-store')
        self.end_headers()
        self.wfile.write(content)

    def do_GET(self):
        if self.path in ['/', '/index.html']:
            self.send(200,html_page(),'text/html; charset=utf-8')
        elif self.path == '/api/base':
            self.send(200,json.dumps(report(),allow_nan=False).encode(),'application/json')
        else:
            self.send(404,b'Not found','text/plain')

    def do_POST(self):
        if self.path != '/api/run':
            return self.send(404,b'Not found','text/plain')
        try:
            size=int(self.headers.get('Content-Length','0'))
            if not 0<size<10000:raise ValueError('Invalid request size')
            controls=json.loads(self.rfile.read(size))
            if not isinstance(controls,dict):raise ValueError('Expected driver object')
            body=json.dumps(run(controls),allow_nan=False).encode()
            self.send(200,body,'application/json')
        except (ValueError,TypeError,AssertionError) as e:
            self.send(400,json.dumps({'error':str(e)}).encode(),'application/json')


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--port',type=int,default=8501)
    parser.add_argument('--export',action='store_true')
    args=parser.parse_args()
    if args.export:
        target=ROOT/'outputs'/'project1-visible-output.html'
        target.parent.mkdir(parents=True,exist_ok=True)
        target.write_bytes(html_page())
        print(f'Saved executed base, statements, checks and sensitivities: {target}')
    else:
        print(f'COHR workbench: http://127.0.0.1:{args.port} (Ctrl+C to stop)',flush=True)
        ThreadingHTTPServer(('127.0.0.1',args.port),Handler).serve_forever()
