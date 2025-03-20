# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, BackstagePass, Sulfuras, Conjured


class TestItem(unittest.TestCase):
    # Day Passes Test
    
    # Test Case 1: Test Normal Item Before Sell_In Date
    def test_normal_before_sell_date(self):
        item = Item("Normal Item", 10, 20)
        item.update_quality()
        self.assertEqual(item.sell_in, 9)
        self.assertEqual(item.quality, 19)

    # Test Case 2: Test Normal Item After Sell_In Date
    def test_normal_after_sell_date(self):
        item = Item("Normal Item 2", -1, 20)
        item.update_quality()
        self.assertEqual(item.sell_in, -2)
        self.assertEqual(item.quality, 18)  # Decreases by 2

    # Test Case 2b: Test Normal Item doesn't subsceed 0 quality
    def test_normal_quality_not_less_than_zero(self):
        item = Item("Normal Item 3", -1, 1)
        item.update_quality()
        self.assertEqual(item.sell_in, -2)
        self.assertEqual(item.quality, 0)    

    # Test Case 3: Test Back Stage quality increase 
    #Increase By 1 when less when more than 10 days sellin
    def test_backstage_after_ten_days(self):
          item = BackstagePass("Age Brie", 13, 20)
          item.update_quality()
          self.assertEqual(item.sell_in, 12)
          self.assertEqual(item.quality, 21)

    #Increase by 2 when sellin is 10 or less days 
    def test_backstage_within_ten_days(self):
        item = BackstagePass("Age Brie 2", 8, 24)
        item.update_quality()
        self.assertEqual(item.sell_in, 7)
        self.assertEqual(item.quality, 26)

    # Increase by 3 when sellin is 5 days or less
    def test_backstage_within_five_days(self):
        item = BackstagePass("Age Brie 3", 3, 34)
        item.update_quality()
        self.assertEqual(item.sell_in, 2)
        self.assertEqual(item.quality, 37)

    # Test Case 4: Test BackStage max quality
    def test_backstage_max_quality(self):
        item = BackstagePass("Age Brie 3", 3, 48)
        item.update_quality()
        self.assertEqual(item.sell_in, 2)
        self.assertEqual(item.quality, 50)

    # Test Case 6: Test BackStage Pass for after concert
    def test_backstage_after_concert(self):
        item = BackstagePass("Age Brie 4", -1, 20)
        item.update_quality()
        self.assertEqual(item.sell_in, -2)
        self.assertEqual(item.quality, 0)

    # Test Case 7: Test Sulfras to ensure no quality change
    def test_sulfuras_no_quality_change(self):
        item = Sulfuras("Sulfuras", 0, 80)
        item.update_quality()
        self.assertEqual(item.sell_in, -1)
        self.assertEqual(item.quality, 80)

    # Test Case 8: Test Conjured Items After Sell in Date
    def test_conjured_after_sell_date(self):
        item = Conjured("Conjured", 0, 7)
        item.update_quality()
        self.assertEqual(item.sell_in, -1)
        self.assertEqual(item.quality, 3)

    # Test Case 9: Test Conjured Items Before Sell in Date
    def test_conjured_before_sell_date(self):
        item = Conjured("Conjured", 4, 7)
        item.update_quality()
        self.assertEqual(item.sell_in, 3)
        self.assertEqual(item.quality, 5)

        
if __name__ == '__main__':
    unittest.main()
