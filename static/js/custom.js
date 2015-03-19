/* Theme Name:iDea - Clean & Powerful Bootstrap Theme
 * Author:HtmlCoder
 * Author URI:http://www.htmlcoder.me
 * Author e-mail:htmlcoder.me@gmail.com
 * Version: 1.1.0
 * Created:October 2014
 * License URI:http://support.wrapbootstrap.com/
 * File Description: Place here your custom scripts
 */


//Custom Owl carousel for products categories
//-----------------------------------------------
var carouselItems = 8;
if ($('.owl-carousel').length>0) {
	$(".owl-carousel.carousel").owlCarousel({
		items: carouselItems,
	});
	$(".owl-carousel.carousel-autoplay").owlCarousel({
		items: carouselItems,
	});
	$(".owl-carousel.clients").owlCarousel({
		items: carouselItems,
		autoPlay: true,
		pagination: false,
		itemsDesktopSmall: [992,5],
		itemsTablet: [768,4],
		itemsMobile: [479,3]
	});
	$(".owl-carousel.content-slider").owlCarousel({
		singleItem: true,
		autoPlay: 5000,
		navigation: false,
		navigationText: false,
		pagination: false
	});
	$(".owl-carousel.content-slider-with-controls").owlCarousel({
		singleItem: true,
		autoPlay: false,
		navigation: true,
		navigationText: false,
		pagination: true
	});
	$(".owl-carousel.content-slider-with-controls-autoplay").owlCarousel({
		singleItem: true,
		autoPlay: 5000,
		navigation: true,
		navigationText: false,
		pagination: true
	});
	$(".owl-carousel.content-slider-with-controls-bottom").owlCarousel({
		singleItem: true,
		autoPlay: false,
		navigation: true,
		navigationText: false,
		pagination: true
	});
};