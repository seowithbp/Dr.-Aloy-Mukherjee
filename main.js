document.addEventListener("DOMContentLoaded", () => {
  // Sticky Header functionality
  const header = document.getElementById("header");

  window.addEventListener("scroll", () => {
    if (window.scrollY > 50) {
      header.classList.add("scrolled");
    } else {
      header.classList.add("scrolled");
    }
  });

  // Ensure header is correctly styled on load
  if (window.scrollY > 50) {
    header.classList.add("scrolled");
  }

  // Scroll animation observer (optional for later)
  const observerOptions = {
    root: null,
    rootMargin: "0px",
    threshold: 0.1,
  };

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.style.animationPlayState = "running";
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

    // Events Carousel Logic (Auto-Scroll)
    const eventsTrack = document.getElementById('events-track');
    
    if (eventsTrack) {
        let scrollPosEvents = 0;
        let isHoveringEvents = false;

        // Clone all nodes to make it infinite
        const eventCards = Array.from(eventsTrack.children);
        eventCards.forEach(card => {
            const clone = card.cloneNode(true);
            eventsTrack.appendChild(clone);
        });

        const animateScrollEvents = () => {
            if (!isHoveringEvents) {
                scrollPosEvents += 1; // Speed of scroll
                if (scrollPosEvents >= eventsTrack.scrollWidth / 2) {
                    scrollPosEvents = 0;
                }
                eventsTrack.style.transform = `translateX(-${scrollPosEvents}px)`;
            }
            requestAnimationFrame(animateScrollEvents);
        };

        eventsTrack.addEventListener('mouseenter', () => isHoveringEvents = true);
        eventsTrack.addEventListener('mouseleave', () => isHoveringEvents = false);
        eventsTrack.addEventListener('touchstart', () => isHoveringEvents = true);
        eventsTrack.addEventListener('touchend', () => isHoveringEvents = false);

        requestAnimationFrame(animateScrollEvents);
    }

    // Auto Scrolling Reviews Logic (Infinite Carousel pattern)
    const reviewsTrack = document.getElementById('reviews-track');
    
    if (reviewsTrack) {
        // Clone items for infinite scroll illusion if needed, or simple bounce
        // Here we implement continuous smooth auto-scroll.
        let scrollPos = 0;
        let isHovering = false;

        // Clone all nodes to make it infinite
        const cards = Array.from(reviewsTrack.children);
        cards.forEach(card => {
            const clone = card.cloneNode(true);
            reviewsTrack.appendChild(clone);
        });

        const animateScroll = () => {
            if (!isHovering) {
                scrollPos += 1; // Speed of scroll
                if (scrollPos >= reviewsTrack.scrollWidth / 2) {
                    scrollPos = 0;
                }
                reviewsTrack.style.transform = `translateX(-${scrollPos}px)`;
            }
            requestAnimationFrame(animateScroll);
        };

        reviewsTrack.addEventListener('mouseenter', () => isHovering = true);
        reviewsTrack.addEventListener('mouseleave', () => isHovering = false);

        requestAnimationFrame(animateScroll);
        
        // Basic touch handling to pause auto scroll
        reviewsTrack.addEventListener('touchstart', () => isHovering = true);
        reviewsTrack.addEventListener('touchend', () => isHovering = false);
    }

    // FAQ Accordion Logic
    const faqQuestions = document.querySelectorAll('.faq-question');
    
    if (faqQuestions) {
        faqQuestions.forEach(question => {
            question.addEventListener('click', () => {
                const parentItem = question.parentElement;
                const answer = question.nextElementSibling;
                
                // Close all others
                document.querySelectorAll('.faq-item').forEach(item => {
                    if (item !== parentItem) {
                        item.classList.remove('active');
                        item.querySelector('.faq-answer').style.maxHeight = null;
                    }
                });

                // Toggle current
                parentItem.classList.toggle('active');
                if (parentItem.classList.contains('active')) {
                    answer.style.maxHeight = answer.scrollHeight + "px";
                } else {
                    answer.style.maxHeight = null;
                }
            });
        });
    }

    // Video Lightbox Logic
    const videoCards = document.querySelectorAll('.video-card');
    const lightbox = document.getElementById('video-lightbox');
    const lightboxIframe = document.getElementById('lightbox-iframe');
    const closeLightbox = document.querySelector('.close-lightbox');

    if (videoCards.length > 0 && lightbox && lightboxIframe && closeLightbox) {
        videoCards.forEach(card => {
            card.addEventListener('click', () => {
                const videoUrl = card.getAttribute('data-video');
                if (videoUrl) {
                    const separator = videoUrl.includes('?') ? '&' : '?';
                    lightboxIframe.src = `${videoUrl}${separator}autoplay=1`;
                    lightbox.classList.add('active');
                }
            });
        });

        closeLightbox.addEventListener('click', () => {
            lightbox.classList.remove('active');
            lightboxIframe.src = ''; 
        });

        // Close when clicking outside the video content
        lightbox.addEventListener('click', (e) => {
            if (e.target === lightbox) {
                lightbox.classList.remove('active');
                lightboxIframe.src = '';
            }
        });
    }

    // Auto Scrolling Videos Logic
    const videosTrack = document.getElementById('videos-track');
    
    if (videosTrack) {
        let scrollPosVideos = 0;
        let isHoveringVideos = false;

        // Clone all nodes to make it infinite
        const videoCardsArray = Array.from(videosTrack.children);
        videoCardsArray.forEach(card => {
            const clone = card.cloneNode(true);
            // Must re-attach event listener to clones for lightbox to work on duplicated cards
            clone.addEventListener('click', () => {
                const videoUrl = clone.getAttribute('data-video');
                if (videoUrl && lightboxIframe && lightbox) {
                    const separator = videoUrl.includes('?') ? '&' : '?';
                    lightboxIframe.src = `${videoUrl}${separator}autoplay=1`;
                    lightbox.classList.add('active');
                }
            });
            videosTrack.appendChild(clone);
        });

        const animateScrollVideos = () => {
            if (!isHoveringVideos) {
                scrollPosVideos += 1; // Speed of scroll
                if (scrollPosVideos >= videosTrack.scrollWidth / 2) {
                    scrollPosVideos = 0;
                }
                videosTrack.style.transform = `translateX(-${scrollPosVideos}px)`;
            }
            requestAnimationFrame(animateScrollVideos);
        };

        videosTrack.addEventListener('mouseenter', () => isHoveringVideos = true);
        videosTrack.addEventListener('mouseleave', () => isHoveringVideos = false);
        videosTrack.addEventListener('touchstart', () => isHoveringVideos = true);
        videosTrack.addEventListener('touchend', () => isHoveringVideos = false);

        requestAnimationFrame(animateScrollVideos);
    }

    // Mobile Menu Toggle
    const hamburger = document.querySelector(".hamburger");
    const navList = document.querySelector(".nav-list");

    if (hamburger && navList) {
        hamburger.addEventListener("click", () => {
            navList.classList.toggle("active");
            const icon = hamburger.querySelector("i");
            if (navList.classList.contains("active")) {
                icon.classList.remove("fa-bars");
                icon.classList.add("fa-times");
            } else {
                icon.classList.remove("fa-times");
                icon.classList.add("fa-bars");
            }
        });

        // Close menu when a link is clicked
        const navLinks = document.querySelectorAll(".nav-link:not(.dropdown-toggle)");
        navLinks.forEach(link => {
            link.addEventListener("click", () => {
                navList.classList.remove("active");
                if (hamburger.querySelector("i") && hamburger.querySelector("i").classList.contains("fa-times")) {
                    hamburger.querySelector("i").classList.remove("fa-times");
                    hamburger.querySelector("i").classList.add("fa-bars");
                }
            });
        });
    }

});

