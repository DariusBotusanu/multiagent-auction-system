import asyncio
import random
from auction.auctioneer import Auctioneer
from auction.seller import Seller
from auction.buyer import Buyer

async def run_single_auction(auction_id):
    # Initialize the seller with product details, initial price, and reserve price
    seller = Seller(f"Antique Vase {auction_id}", initial_price=100, reserve_price=150)

    # Initialize buyers with random budgets
    buyers = [Buyer(name=f"Buyer{i+1}", budget=random.randint(50, 200)) for i in range(5)]

    # Create the auctioneer to manage the auction process
    auctioneer = Auctioneer(seller, buyers)

    # Start the auction
    await auctioneer.start_auction()
    result = {
        'auction_id': auction_id,
        'item_name': seller.item_name,
        'highest_bid': seller.highest_bid,
        'highest_bidder': seller.highest_bidder,
        'auction_complete': seller.auction_complete
    }
    return result

async def main(num_auctions):
    auction_tasks = [run_single_auction(i) for i in range(num_auctions)]
    results = await asyncio.gather(*auction_tasks)
    for result in results:
        print(f"Auction {result['auction_id']} for {result['item_name']}:")
        if result['auction_complete']:
            print(f"  Sold to {result['highest_bidder']} for {result['highest_bid']}")
        else:
            print("  Did not meet the reserve price")

if __name__ == "__main__":
    num_auctions = 10  # Set the number of auctions to simulate
    asyncio.run(main(num_auctions))

