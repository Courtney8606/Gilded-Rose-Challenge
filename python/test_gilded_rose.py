# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRose, AgedBrie, BackstagePasses, Sulfuras, ConjuredItem, GenericItem


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [GenericItem("food", 0, 0), GenericItem("health potion", 0, 20) ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("food", items[0].name)
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)
        self.assertEqual("health potion", items[-1].name)
        self.assertEqual(-1, items[-1].sell_in)
        self.assertEqual(18, items[-1].quality)

    def test_brie(self):
        items = [AgedBrie("Aged Brie", 6, 25)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Aged Brie", items[0].name)
        self.assertEqual(5, items[0].sell_in)
        self.assertEqual(26, items[0].quality)
    
    def test_backstage_passes(self):
        items = [BackstagePasses("Backstage passes to a TAFKAL80ETC concert", 2, 40), BackstagePasses("Backstage passes to a TAFKAL80ETC concert", 7, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(43, items[0].quality)
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(22, items[-1].quality)
        self.assertEqual(6, items[-1].sell_in)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(25, items[-1].quality)
        self.assertEqual(5, items[-1].sell_in)

    def test_sulfuras(self):
        items = [Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(80, items[0].quality)
    
    def test_conjured_item(self):
        items = [ConjuredItem("Conjured goblet of wealth", 3, 25)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(2, items[0].sell_in)
        self.assertEqual(23, items[0].quality)

        
if __name__ == '__main__':
    unittest.main()
