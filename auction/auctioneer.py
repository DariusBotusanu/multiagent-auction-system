import asyncio

class Auctioneer:
    def __init__(self, seller, buyers):
        """
        Initialize the Auctioneer with a seller and a list of buyers.

        :param seller: The seller agent.
        :param buyers: A list of buyer agents.
        """
        self.seller = seller
        self.buyers = buyers

    async def start_auction(self):
        """
        Start the auction process. Conduct up to three initial rounds of bidding,
        followed by additional bidding rounds if necessary.
        """
        # Conduct up to three initial rounds of bidding
        for round_number in range(1, 4):
            print(f"Starting auction round {round_number}")
            cfp = self.seller.create_cfp()
            
            # Collect bids from all buyers except the highest bidder from the previous round
            tasks = [buyer.receive_cfp(cfp) for buyer in self.buyers if buyer != self.seller.highest_bidder]
            bids = await asyncio.gather(*tasks)
            
            # Print each bid received
            for bid in bids:
                if bid['bid'] > 0:
                    print(f"{bid['name']} bids {bid['bid']}")
            
            # Evaluate the bids and determine if the auction is complete
            self.seller.evaluate_bids(bids)
            if self.seller.auction_complete:
                return
        
        # Conduct additional bidding rounds if the reserve price is not met
        await self.additional_bidding_rounds()
        print("Auction ended without meeting the reserve price.")

    async def additional_bidding_rounds(self):
        """
        Conduct up to three additional bidding rounds ("once", "twice", "thrice") 
        if the reserve price is not met in the initial rounds.
        """
        for attempt in ["once", "twice", "thrice"]:
            print(f"Max bid attempt {attempt}")
            cfp = self.seller.create_cfp()
            
            # Collect bids from all buyers except the highest bidder from the previous round
            tasks = [buyer.receive_cfp(cfp) for buyer in self.buyers if buyer != self.seller.highest_bidder]
            bids = await asyncio.gather(*tasks)
            
            # Print each bid received
            for bid in bids:
                if bid['bid'] > 0:
                    print(f"{bid['name']} bids {bid['bid']}")
            
            # Evaluate the bids and determine if the auction is complete
            self.seller.evaluate_bids(bids)
            if self.seller.auction_complete:
                return
