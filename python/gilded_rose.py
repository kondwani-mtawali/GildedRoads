# -*- coding: utf-8 -*-

# class GildedRose(object):

#     def __init__(self, items):
#         self.items = items

#     def update_quality(self):
#         for item in self.items:
#             if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
#                 if item.quality > 0:
#                     if item.name != "Sulfuras, Hand of Ragnaros":
#                         item.quality = item.quality - 1
#             else:
#                 if item.quality < 50:
#                     item.quality = item.quality + 1
#                     if item.name == "Backstage passes to a TAFKAL80ETC concert":
#                         if item.sell_in < 11:
#                             if item.quality < 50:
#                                 item.quality = item.quality + 1
#                         if item.sell_in < 6:
#                             if item.quality < 50:
#                                 item.quality = item.quality + 1
#             if item.name != "Sulfuras, Hand of Ragnaros":
#                 item.sell_in = item.sell_in - 1
#             if item.sell_in < 0:
#                 if item.name != "Aged Brie":
#                     if item.name != "Backstage passes to a TAFKAL80ETC concert":
#                         if item.quality > 0:
#                             if item.name != "Sulfuras, Hand of Ragnaros":
#                                 item.quality = item.quality - 1
#                     else:
#                         item.quality = item.quality - item.quality
#                 else:
#                     if item.quality < 50:
#                         item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
    
    def day_passes(self):
        self.sell_in -= 1

    def update_quality(self):
        self.day_passes()
        if self.quality > 0:
            if self.sell_in <= 0: #If sell date has passed, quality decreases by 2
                self.quality = max(self.quality - 2, 0)

            else: 
                self.quality = max(self.quality - 1, 0)
            
    
class BackstagePass(Item):
    def update_quality(self):
        self.day_passes()
        # I don't understand what quality drops to 0 after concert is entailing???
        if self.sell_in <= 0:
            self.quality = 0

        elif self.sell_in <= 5: #Increments quality by 3 when 5 days or less
            self.quality = min(self.quality + 3, 50) 

        elif self.sell_in <= 10: #Increments quality by 2 when 10 days or less
            self.quality = min(self.quality + 2, 50) 
        else: 
            self.quality = min(self.quality + 1, 50)
        
class Sulfuras(Item): 
    Item.quality = 80
    def update_quality(self):
        self.day_passes()
        

class Conjured(Item): 
    def update_quality(self):
        self.day_passes()
        if self.sell_in <= 0:
            self.quality = max(self.quality - 4, 0)
        
        else:
            self.quality = max(self.quality - 2, 0)
