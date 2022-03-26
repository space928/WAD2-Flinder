// Swipeable deck of cards implementation
// Based off: https://github.com/simonepm/likecarousel available
// under the MIT license

class Swiper {
    constructor(rootElement) {
        this.board = rootElement;
        this.updateCards();
    }

    updateCards() {
        this.cards = this.board.getElementsByClassName("swiper-card");
        if(this.cards.length > 0) {
            const topCard = this.cards[this.cards.length-1];
            topCard.style.transform = "translateX(-50%) translateY(-50%) rotate(0deg) rotateY(0deg) scale(1)";

            // Destroy the old Hammer instance
            if(this.hammer) this.hammer.destroy();

            this.hammer = new Hammer(topCard);
            this.hammer.add(new Hammer.Tap());
            this.hammer.add(new Hammer.Pan({
                position: Hammer.position_ALL,
                threshold: 0
            }));

            // Create event handlers
            this.hammer.on('tap', (e) => {
                this.onTap(e)
            });
            this.hammer.on('pan', (e) => {
                this.onPan(e)
            });
        }
    }

    onTap (e) {

    }

    onPan(e) {

    }
}