# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update_quality()

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class AgedBrie(Item):
    def update_quality(self):
        self.sell_in -= 1
        if self.quality < 50:
            self.quality += 1

class BackstagePasses(Item):
    def update_quality(self):
        self.sell_in -= 1
        if self.sell_in >= 11:
            self.quality += 1
        if self.sell_in < 11 and self.sell_in >= 6:
            increment = 2
            if self.quality + increment > 50:
                self.quality = 50
            else:
                self.quality += increment
        if self.sell_in < 6:
            increment = 3
            if self.quality + increment > 50:
                self.quality = 50
            else:
                self.quality += increment
        if self.sell_in <= 0:
            self.quality = 0
        

class Sulfuras(Item):
    def update_quality(self):
            self.quality = 80
            self.sell_in = 0

class ConjuredItem(Item):
    def update_quality(self):
        self.sell_in -= 1
        if self.quality > 0:
            if self.sell_in > 0:
                decrement = 2
                if (self.quality - decrement) < 0:
                    self.quality = 0 
                else:
                    self.quality = self.quality - 2
            if self.sell_in < 0:
                decrement = 4
                if (self.quality - decrement) < 0:
                    self.quality = 0 
                else:
                    self.quality = self.quality - decrement
        

class GenericItem(Item):
    def update_quality(self):
        self.sell_in -= 1
        if self.quality > 0:
            if self.sell_in > 0:
                self.quality -= 1
            if self.sell_in < 0:
                decrement = 2
                if (self.quality - decrement) < 0:
                    self.quality = 0 
                else:
                    self.quality -= decrement
        