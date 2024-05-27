import random
import asyncio

class Buyer:
    def __init__(self, name, budget):
        """
        Initialize a Buyer with a name and a budget.

        :param name: The name of the buyer.
        :param budget: The budget available to the buyer for bidding.
        """
        self.name = name
        self.budget = budget
        self.current_bid = 0

    async def receive_cfp(self, cfp):
        """
        Handle the reception of a Call For Proposal (CFP) from the seller.
        This function simulates asynchronous behavior to mimic real-world conditions.

        :param cfp: A dictionary containing the current price and item details from the seller.
        :return: A dictionary containing the buyer's name and their bid.
        """
        # Simulate a delay to represent asynchronous bid processing
        await asyncio.sleep(random.uniform(0.1, 1.0))
        
        # Store the CFP details
        self.cfp = cfp
        
        # Make a bid based on the received CFP
        return self.make_bid()

    def make_bid(self):
        """
        Make a bid in response to the CFP. The bid is a random value between the current price and the buyer's budget,
        provided the budget is sufficient to cover the current price.

        :return: A dictionary containing the buyer's name and their bid amount.
        """
        if self.budget >= self.cfp['current_price']:
            # Generate a random bid within the buyer's budget limits
            bid = random.randint(self.cfp['current_price'], self.budget)
            self.current_bid = bid
            return {'name': self.name, 'bid': bid}
        
        # If the budget is insufficient, the bid is 0
        return {'name': self.name, 'bid': 0}

