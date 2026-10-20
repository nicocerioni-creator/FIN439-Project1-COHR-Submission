"""Targeted finance checks; these are AI-assisted, not the locked human test."""
from copy import deepcopy
import unittest
from engine import run, sensitivity, discounted_fcff, lab


class FinanceTests(unittest.TestCase):
    def test_official_course_training_answers(self):
        # Published Lab 05 table, retrieved October 19, 2026:
        # https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-03/lab-05-dcf-build.md
        path=[];cf=100
        for growth in [.08,.06,.05,.04,.03]:
            cf*=1+growth;path.append(cf)
        v=discounted_fcff(path,.10,.03,path[-1]*1.03,[1,2,3,4,5])
        actual=[*path,v['explicit_pv'],v['terminal_value'],v['terminal_pv'],
                v['enterprise_value'],v['enterprise_value']+50-300,
                (v['enterprise_value']+50-300)/50,v['terminal_share']]
        expected=[108,114.48,120.204,125.0122,128.7625,448.4408,1894.6486,
                  1176.4277,1624.8685,1374.8685,27.4974,.7240]
        for observed,known in zip(actual,expected):self.assertAlmostEqual(observed,known,delta=.0001)
        for w,g,expected_price in [(.09,.02,28.60),(.09,.04,39.02),(.11,.02,21.06),(.11,.04,26.44)]:
            grid=discounted_fcff(path,w,g,path[-1]*(1+g),[1,2,3,4,5])
            self.assertAlmostEqual((grid['enterprise_value']+50-300)/50,expected_price,delta=.01)

    def test_known_answer_annuity_and_negative_cash(self):
        # Five 100 payments plus a zero-growth perpetuity are worth 100/.10.
        v = discounted_fcff([100]*5, .10, 0, 100, [1,2,3,4,5])
        self.assertAlmostEqual(v['enterprise_value'], 1000)
        negative = discounted_fcff([-100,100,100,100,100], .10, 0, 100, [1,2,3,4,5])
        self.assertAlmostEqual(v['enterprise_value']-negative['enterprise_value'],200/1.1)

    def test_articulation_identity_bridge_and_restore(self):
        before = deepcopy(lab.ASSUMPTIONS)
        b = run()
        self.assertTrue(b['all_checks_pass'])
        run({'margin_shift_pp': 1})
        self.assertEqual(b,run())
        self.assertEqual(before,lab.ASSUMPTIONS)
        self.assertLess(b['statements'][0]['fcff'],0)
        self.assertAlmostEqual(b['valuation']['equity_value']+b['bridge']['net_claims'],b['valuation']['enterprise_value'])

    def test_predeclared_financial_directions(self):
        # Predictions authored by Codex before this test's first execution:
        # +margin increases EBIT and value; +WACC reduces value; +g raises value
        # over this bounded domain. These are NOT student AI-off predictions.
        b=run()
        m=run({'margin_shift_pp':1})
        self.assertGreater(m['statements'][-1]['operating_income'],b['statements'][-1]['operating_income'])
        self.assertGreater(m['valuation']['per_share'],b['valuation']['per_share'])
        for g in [2,3,4]:
            prices=[run({'wacc_pct':w,'terminal_growth_pct':g})['valuation']['per_share'] for w in [9,10,11,12,13]]
            self.assertTrue(all(a>b for a,b in zip(prices,prices[1:])))
        for w in [9,10,11,12,13]:
            prices=[run({'wacc_pct':w,'terminal_growth_pct':g})['valuation']['per_share'] for g in [2,3,4]]
            self.assertTrue(all(a<b for a,b in zip(prices,prices[1:])))

    def test_real_funding_failure_and_bad_input_rejected(self):
        stressed=run({'growth_shift_pp':5})
        self.assertFalse(stressed['all_checks_pass'])
        self.assertTrue(any(not x['pass'] and 'cash_floor_shortfall' in x['check'] for x in stressed['checks']))
        for values in [{'wacc_pct':float('nan')},{'margin_shift_pp':3},{'unknown':1}]:
            with self.assertRaises(ValueError):run(values)
        with self.assertRaises(ValueError):discounted_fcff([100]*5,.03,.03,100,[1,2,3,4,5])

    def test_reverse_price_reconstruction(self):
        b=run();v=b['valuation'];w=b['assumptions']['wacc'];g=b['assumptions']['terminal_growth']
        ev=v['explicit_pv']+v['reverse_dcf']['required_terminal_fcff']/(w-g)/(1+w)**v['discount_times'][-1]
        self.assertAlmostEqual((ev-b['bridge']['net_claims'])/b['shares_million'],b['market_price'])


if __name__=='__main__':unittest.main(verbosity=2)
