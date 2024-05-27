import random
import asyncio

class Seller:
    def __init__(self, item_name, initial_price, reserve_price):
        """
        Initialize the Seller with the item details, initial price, and reserve price.

        :param item_name: The name of the item being auctioned.
        :param initial_price: The starting price for the auction.
        :param reserve_price: The minimum price required to sell the item.
        """
        self.item_name = item_name
        self.current_price = initial_price
        self.reserve_price = reserve_price
        self.auction_complete = False
        self.highest_bid = 0
        self.highest_bidder = None

    def create_cfp(self):
        """
        Create a Call For Proposal (CFP) to send to buyers, containing the item name and the current price.

        :return: A dictionary containing the item name and the current price.
        """
        print(f"CFP: {self.item_name} starting at {self.current_price}")
        return {'item_name': self.item_name, 'current_price': self.current_price}

    def evaluate_bids(self, bids):
        """
        Evaluate the bids received from buyers and determine the highest bid.
        If the highest bid meets or exceeds the reserve price, the auction is marked as complete.

        :param bids: A list of dictionaries containing bids from buyers.
        """
        # Determine the highest bid from the received bids
        highest_bid = max(bids, key=lambda x: x['bid'])

        # Update the highest bid and highest bidder if the new bid is higher
        if highest_bid['bid'] > self.highest_bid:
            self.highest_bid = highest_bid['bid']
            self.highest_bidder = highest_bid['name']

        # Check if the highest bid meets or exceeds the reserve price
        if self.highest_bid >= self.reserve_price:
            self.auction_complete = True
            print(f"Item sold to {self.highest_bidder} for {self.highest_bid}")
        else:
            # Update the current price to the highest bid if the reserve price is not met
            self.current_price = self.highest_bid

