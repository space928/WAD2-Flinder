// Swipeable deck of cards implementation
// Based on: https://github.com/simonepm/likecarousel available
// under the MIT license

class Swiper {
    constructor(rootElement, transitionTime, swipeThreshold, maxRotation, scaleChange) {
        this.board = rootElement;
        this.transitionTime = transitionTime;
        this.swipeThreshold = swipeThreshold;
        this.maxRotation = maxRotation;
        this.scaleChange = scaleChange;
        this.updateCards();
        this.onCardSwiped = null;
        this.onHeld = null;
        this.onRelease = null;
    }

    swipeCurrent(direction) {
        let posX = direction?(this.board.clientWidth):(-(this.board.clientWidth + this.topCard.clientWidth));
        let rot = direction?(this.maxRotation):(-this.maxRotation);

        // Set transition properties
        this.topCard.style.transition = `transform ${this.transitionTime*2}ms ease-out`;
        if(this.nextCard)
            this.nextCard.style.transition = `transform ${this.transitionTime}ms linear`;

        // Throw away the card
        this.topCard.style.transform =
            `translateX(${posX}px) translateY(${0}px) rotate(${rot}deg)`;

        // Wait for the transition, then remove the card
        setTimeout(() => {
            if(this.onCardSwiped)
                this.onCardSwiped(this.topCard, direction);

            this.board.removeChild(this.topCard);

            this.updateCards();
        }, this.transitionTime*2);
    }

    updateCards() {
        this.cards = this.board.children;
        if(this.cards.length > 0) {
            this.topCard = this.cards[this.cards.length-1];
            this.topCard.style.transform = "translateX(-50%) translateY(-50%) rotate(0deg) rotateY(0deg) scale(1)";

            if(this.cards.length > 1)
                this.nextCard = this.cards[this.cards.length-2];

            // Destroy the old Hammer instance
            if(this.hammer) this.hammer.destroy();

            this.hammer = new Hammer(this.topCard);
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
        // Jump the card to the position of the tap
        const x = (e.center.x - e.target.getBoundingClientRect().left) / e.target.clientWidth;
        const rotY = this.maxRotation/3 * (x < 0.05 ? -1 : 1);
        // Enable transition
        this.topCard.style.transition = `transform ${this.transitionTime}ms ease-out`;

        this.topCard.style.transform =
            "translateX(-50%) translateY(-50%) rotate(0deg) rotateY(" + rotY + "deg) scale(1)";

        // After the transition, reset the transform
        setTimeout(() => {
            this.topCard.style.transform =
                        "translateX(-50%) translateY(-50%) rotate(0deg) rotateY(0deg) scale(1)";
        }, this.transitionTime);
    }

    onPan(e) {
        if(!this.isPanning) {
            // First frame of panning
            this.isPanning = true;

            // Reset transitions
            this.topCard.style.transition = null;
            if(this.nextCard)
                this.nextCard.style.transition = null;

            // Get starting pos
            let style = window.getComputedStyle(this.topCard);
            let mx = style.transform.match(/^matrix\((.+)\)$/);
            this.startPosX = mx ? parseFloat(mx[1].split(', ')[4]) : 0;
            this.startPosY = mx ? parseFloat(mx[1].split(', ')[5]) : 0;

            let bounds = this.topCard.getBoundingClientRect();

            this.isDraggingFrom =
                (e.center.y - bounds.top) > this.topCard.clientHeight / 2 ? -1 : 1;

            if(this.onHeld)
                this.onHeld(this.topCard);
        }

        // Compute next position of card
        let posX = e.deltaX + this.startPosX;
        let posY = e.deltaY + this.startPosY;
        let ratioX = e.deltaX / this.board.clientWidth;
        let ratioY = e.deltaY / this.board.clientHeight;
        let swipeDir = e.deltaX < 0 ? -1 : 1;
        let rot = this.isDraggingFrom * swipeDir * Math.abs(ratioX) * this.maxRotation;
        let nextScale = (1-this.scaleChange + (this.scaleChange * Math.abs(ratioX)));

        // Set the new position
        this.topCard.style.transform =
            `translateX(${posX}px) translateY(${posY}px) rotate(${rot}deg) rotateY(${ratioX*this.maxRotation}deg) rotateX(${-ratioY*this.maxRotation}deg) scale(1)`;
        // Update the scale of the next card
        if(this.nextCard)
            this.nextCard.style.transform =
                `translateX(-50%) translateY(-50%) rotate(0deg) rotateY(0deg) scale(${nextScale})`;

        // Last frame of swiping
        if(e.isFinal) {
            if(this.onRelease)
                this.onRelease(this.topCard);
            this.isPanning = false;
            let successful = false;

            // Reset transition properties
            this.topCard.style.transition = `transform ${this.transitionTime*2}ms ease-out`;
            if(this.nextCard)
                this.nextCard.style.transition = `transform ${this.transitionTime}ms linear`;

            // Check swiping threshold to work out if the card has been successfully swiped
            if(ratioX > this.swipeThreshold && e.direction === Hammer.DIRECTION_RIGHT) {
                successful = true;
                posX = this.board.clientWidth;
            } else if (ratioX < -this.swipeThreshold && e.direction === Hammer.DIRECTION_LEFT) {
                successful = true;
                posX = -(this.board.clientWidth + this.topCard.clientWidth);
            }

            if (successful) {
                // Throw away the card
                this.topCard.style.transform =
                    `translateX(${posX}px) translateY(${posY}px) rotate(${rot}deg)`;

                // Wait for the transition, then remove the card
                setTimeout(() => {
                    if(this.onCardSwiped)
                        this.onCardSwiped(this.topCard, e.direction === Hammer.DIRECTION_RIGHT);

                    this.board.removeChild(this.topCard);

                    this.updateCards();
                }, this.transitionTime*2);
            } else {
                // Reset the cards position
                this.topCard.style.transform =
                    'translateX(-50%) translateY(-50%) rotate(0deg) rotateY(0deg) scale(1)';
                if (this.nextCard)
                    this.nextCard.style.transform =
                        `translateX(-50%) translateY(-50%) rotate(0deg) rotateY(0deg) scale(${1-this.scaleChange})`;
            }
        }
    }
}