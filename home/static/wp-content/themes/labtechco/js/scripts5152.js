/**
 * Functionality specific to LabtechCO.
 *
 * Provides helper functions to enhance the theme experience.
 */

"use strict";

/*------------------------------------------------------------------------------*/
/* Back to top
/*------------------------------------------------------------------------------*/

// ===== Scroll to Top ==== 
jQuery('#totop').hide();
jQuery(window).scroll(function() {
    if (jQuery(this).scrollTop() >= 100) {        // If page is scrolled more than 50px
        jQuery('#totop').fadeIn(200);    // Fade in the arrow
        jQuery('#totop').addClass('top-visible');
    } else {
        jQuery('#totop').fadeOut(200);   // Else fade out the arrow
        jQuery('#totop').removeClass('top-visible');
    }
});
jQuery('#totop').on('click', function() {      // When arrow is clicked
    jQuery('body,html').animate({
        scrollTop : 0                       // Scroll to top of body
    }, 500);
    return false;
});







/*------------------------------------------------------------------------------*/
/* Equal Height Div
/*------------------------------------------------------------------------------*/

var equalheight = function(container){

var currentTallest = 0,
     currentRowStart = 0,
     rowDivs = new Array(),
     $el,
     topPosition = 0;
 jQuery(container).each(function() {

   $el = jQuery(this);
   jQuery($el).outerHeight('auto')
   topPostion = $el.position().top;

   if (currentRowStart != topPostion) {
     for (currentDiv = 0 ; currentDiv < rowDivs.length ; currentDiv++) {
       rowDivs[currentDiv].height(currentTallest);
     }
     rowDivs.length = 0; // empty the array
     currentRowStart = topPostion;
     currentTallest = $el.outerHeight();
     rowDivs.push($el);
   } else {
     rowDivs.push($el);
     currentTallest = (currentTallest < $el.outerHeight()) ? ($el.outerHeight()) : (currentTallest);
  }
   for (currentDiv = 0 ; currentDiv < rowDivs.length ; currentDiv++) {
     rowDivs[currentDiv].outerHeight(currentTallest);
   }
 });
}	

function ts_sticky(){
	
	if( typeof jQuery.fn.stick_in_parent == "function" ){
		
		// Admin bar
		var offset_px = 0;
		if( jQuery('body').hasClass('admin-bar') ){
			offset_px = jQuery('#wpadminbar').height();
		}
		
		// Returns width of browser viewport
		var pageWidth = jQuery( window ).width();	
		// setting height for spacer
		if( parseInt(pageWidth) > parseInt(ts_breakpoint) ){
			jQuery('.ts-stickable-header').stick_in_parent({'parent':'body', 'spacer':false, 'offset_top':offset_px });
		} else {
			jQuery('.ts-stickable-header').trigger("sticky_kit:detach");
		}
	
	}
}


function themestek_setCookie(c_name,value,exdays){
	var now  = new Date();
	var time = now.getTime();
	time    += (3600 * 1000) * 24;
	now.setTime(time);

	var c_value=escape(value) + ((exdays==null) ? "" : "; expires="+now.toGMTString() );
	document.cookie=c_name + "=" + c_value;
} // END function themestek_setCookie





/*------------------------------------------------------------------------------*/
/* YITH Wishlist plugin - modifying JS code so it will work differently
/*------------------------------------------------------------------------------*/
function themestek_yith_wishlist_func(){
	/*wishlist js*/
	jQuery(document).off("click", ".add_to_wishlist");

	jQuery(document).on("click", ".add_to_wishlist", function() {

		var b = yith_wcwl_plugin_ajax_web_url;
		var opts = {
			add_to_wishlist: jQuery(this).data("product-id"),
			product_type: jQuery(this).data("product-type"),
			action: "add_to_wishlist"
		};
		mgk_yith_ajax_wish_list(jQuery(this), b, opts);
		return false;
	});

	var mgk_yith_ajax_wish_list = function(obj, ajaxurl, opts) {
		jQuery.ajax({
			type: "POST",
			url: ajaxurl,
			data: "product_id=" + opts.add_to_wishlist + "&" + jQuery.param(opts),
			dataType: 'json',
			success: function(resp) {
				response_result = resp.result,
					response_message = resp.message;
				jQuery('body .main-holder div#notification').remove();
				var ntop = jQuery('#wpadminbar') !== undefined ? jQuery('#wpadminbar').height() : 10;
				
				// getting main object to select it's class
				var mainObj = obj.closest('.yith-wcwl-add-to-wishlist');
				
				if (response_result == 'true') {
					
					if (MGK_ADD_TO_WISHLIST_SUCCESS_TEXT !== undefined)
						jQuery('<div id="notification" class="row"><div class="success">' + MGK_ADD_TO_WISHLIST_SUCCESS_TEXT + '<img class="close" alt="" src="' + IMAGEURL + '/close.png"></div></div>').prependTo('body .main-holder');
					jQuery('body .main-holder div#notification').css('top', ntop + 'px');
					jQuery('body .main-holder div#notification > div').fadeIn('show');
					
					
					jQuery('.yith-wcwl-add-button', mainObj).addClass('ts-hide').hide();
					jQuery('.yith-wcwl-wishlistexistsbrowse', mainObj).addClass('ts-show').show();  // Show GoTo Wishlist button now
					
					jQuery('.yith-wcwl-add-button', mainObj).attr('style','display: none !important');
					jQuery('.yith-wcwl-wishlistexistsbrowse', mainObj).attr('style','display: block !important');
					
					
					jQuery('html,body').animate({
						scrollTop: 0
					}, 300);
					
				} else if (response_result == 'exists') {
					if (MGK_ADD_TO_WISHLIST_EXISTS_TEXT !== undefined)
						jQuery('<div id="notification" class="row"><div class="success">' + MGK_ADD_TO_WISHLIST_EXISTS_TEXT + '<img class="close" alt="" src="' + IMAGEURL + '/close.png"></div></div>').prependTo('body .main-holder');
					jQuery('body .main-holder div#notification').css('top', ntop + 'px');
					jQuery('body .main-holder div#notification > div').fadeIn('show');					
					
					jQuery('.yith-wcwl-add-button', mainObj).attr('style','display: none !important');  // hide original button
					
					jQuery('.yith-wcwl-wishlistexistsbrowse', mainObj).attr('style','display: show !important');  // Show already exists in wishlist message
					
					jQuery('html,body').animate({
						scrollTop: 0
					}, 300);

				}
				setTimeout(function() {
					removeNft();
				}, 10000);

			}
		});
	};

	var removeNft = function() {
		if (jQuery("#notification") !== undefined)
			jQuery("#notification").remove();
	};

};




/*------------------------------------------------------------------------------*/
/* Function to set dynamic height of Testimonial columns
/*------------------------------------------------------------------------------*/
function setHeight(column) {
    var maxHeight = 0;
    //Get all the element with class = col
    column = jQuery(column);
    column.css('height', 'auto');
	
	// Responsive condition: Work only in tablet, desktop and other bigger devices.
	if( jQuery( window ).width() > 479 ){
		
		//Loop all the column
		column.each(function() {       
			//Store the highest value
			if(jQuery(this).height() > maxHeight) {
				maxHeight = jQuery(this).height();
			}
		});
		//Set the height
		column.height(maxHeight);
		
	} // if( jQuery( window ).width() > 479 )
} // END function setHeight
/**************************************************************************/






/*------------------------------------------------------------------------------*/
/* Search form on search results page
/*------------------------------------------------------------------------------*/
function themestek_search_form(){
	if( jQuery('.ts-search-form-wrapper').length>0 ){
		
		jQuery('.ts-search-form-tab > a').on('click', function(e){
			var mainele = jQuery(this).closest('.ts-search-form-wrapper');
			var cpt     = jQuery(this).data('cpt');
			jQuery('input[name="post_type"]', mainele).val( cpt );
			jQuery('form.ts-search-form').submit();
			e.preventDefault();
		});
	}
}





/*------------------------------------------------------------------------------*/
/* Function to Set Blog Masonry view
/*------------------------------------------------------------------------------*/
function themestek_blogmasonry(){
	if( jQuery().isotope ){
		if( jQuery('#content.themestek-blog-col-page').length > 0 ){
			
			jQuery('#content.themestek-blog-col-page').masonry();
			jQuery('#content.themestek-blog-col-page').isotope({
					itemSelector: '.post-box',
					masonry: {
							
					},
					sortBy : 'original-order'
			});
		}
	}
}
/*------------------------------------------------------------------------------*/
/* Function to set margin bottom for sticky footer
/*------------------------------------------------------------------------------*/
function themestek_stickyFooter(){
	if( jQuery('body').hasClass('themestek-sticky-footer')){
		jQuery('div#content-wrapper').css( 'marginBottom', jQuery('footer#colophon').height() );
	}
}


/*------------------------------------------------------------------------------*/
/* Function to add class to select box if default option selected
/*------------------------------------------------------------------------------*/
function setEmptySelectBox(element){
	if(jQuery(element).val() == ""){
		jQuery(element).addClass("empty");
	} else {
		jQuery(element).removeClass("empty");
	}
}

function ts_hide_togle_link(){
	if( jQuery('#navbar div.mega-menu-wrap ul.mega-menu').length > 0 ){
		jQuery('h3.menu-toggle').css('display','none');
	}
}

/*------------------------------------------------------------------------------*/
/* Google Map in Header area
/*------------------------------------------------------------------------------*/
function themestek_reset_gmap(){
	jQuery('.themestek-fbar-box-w > div > aside').each(function(){
		var mainthis = jQuery(this);
		jQuery( 'iframe[src^="https://www.google.com/maps/"], iframe[src^="http://www.google.com/maps/"]',mainthis ).each(function(){
			if( !jQuery(this).hasClass('themestek-set-gmap') ){
				jQuery(this).attr('src',jQuery(this).attr('src')+'');
				jQuery(this).on( 'load', function(){
					jQuery(this).addClass('themestek-set-gmap').animate({opacity: 1 }, 1000 );
				});	

			}
		})
	});
}
function themestek_hide_gmap(){
	jQuery('.themestek-fbar-box-w > div > aside').each(function(){
		var mainthis = jQuery(this);
		jQuery( 'iframe[src^="https://www.google.com/maps/"], iframe[src^="http://www.google.com/maps/"]',mainthis ).each(function(){
			if( !jQuery(this).hasClass('themestek-set-gmap') ){
				jQuery(this).css({opacity: 0});				
				jQuery(this).css('display', 'block');
			}
		})
	});
}	
	

function themestek_isotope() {
	jQuery('.themestek-boxes-sortable-yes').each(function(){	
		var gallery_item = jQuery('.themestek-boxes-row-wrapper', this );
		var filterLinks  = jQuery('.ts-sortable-wrapper a', this );			
		gallery_item.isotope({
			animationEngine : 'best-available',
			layoutMode : 'fitRows'
		})
		filterLinks.on('click', function(e){
			var selector = jQuery(this).attr('data-filter');
			gallery_item.isotope({
				filter : selector,
				itemSelector : '.isotope-item'
			});

			filterLinks.removeClass('selected');
			jQuery('#filter-by li').removeClass('current-cat');
			jQuery(this).addClass('selected');
			e.preventDefault();
		});
		
	});
};	










function labtechco_logMarginPadding(){
	/**************/
	jQuery('.wpb_column').each(function(){
		if( jQuery(this).hasClass('ts-left-span') ){
			
			// Getting width and padding
			var margin     = jQuery(this).parent().css("padding-left").replace("px", "");
			margin         = parseInt(margin);
			var elewidth   = jQuery(this).css("width").replace("px", "");
			elewidth       = parseInt(elewidth);
			var leftsargin = margin + elewidth;
			var after_inlinecss  = '';
			var before_inlinecss = '';
			// Generating random class
			var randomclass = Math.floor((Math.random() * 1000000) + 1);
			randomclass     = 'labtechco-random-class-' + randomclass;
			
			// adding class to this element
			jQuery(this).addClass(randomclass);
			after_inlinecss += 'padding-left: '+leftsargin+'px;';
			
			
			/* * Background Image * */
			if( jQuery('.vc_column-inner', this).css('background-image')!='none' ){
				var bgimage = jQuery('.vc_column-inner', this).css('background-image');
				jQuery('.vc_column-inner', this).css('background-image','none', '!important');				
				after_inlinecss += 'background-image: '+bgimage+';';
			}
			
			/* * Background Color * */
			if( jQuery('.vc_column-inner', this).css('background-color')!='' || jQuery('.vc_column-inner', this).css('background-color')!='inherit' ){
				var bgcolor = jQuery('.vc_column-inner', this).css('background-color');				
				before_inlinecss += 'background-color: '+bgcolor+';';
			}
			
			
			// Now adding inline style in HEAD tag
			if( after_inlinecss!='' || before_inlinecss!='' ){
				jQuery( "head" ).append( '<style>.'+randomclass+':after{'+after_inlinecss+'} .'+randomclass+':before{'+before_inlinecss+'} .ts-left-span .vc_column-inner{background-image:none !important;}</style>' );
			}
			
			
			
		}
	});
}

function labtechco_logMarginPadding_right(){
	/**************/
	jQuery('.wpb_column').each(function(){
		if( jQuery(this).hasClass('ts-right-span') ){
			
			// Getting width and padding
			var margin     = jQuery(this).parent().css("padding-right").replace("px", "");
			margin         = parseInt(margin);
			var elewidth   = jQuery(this).css("width").replace("px", "");
			elewidth       = parseInt(elewidth);
			var leftsargin = margin + elewidth;
			var after_inlinecss  = '';
			var before_inlinecss = '';
			// Generating random class
			var randomclass = Math.floor((Math.random() * 1000000) + 1);
			randomclass     = 'labtechco-random-class-' + randomclass;
			
			// adding class to this element
			jQuery(this).addClass(randomclass);
			after_inlinecss += 'padding-right: '+leftsargin+'px;';
			
			
			/* * Background Image * */
			if( jQuery('.vc_column-inner', this).css('background-image')!='none' ){
				var bgimage = jQuery('.vc_column-inner', this).css('background-image');
				jQuery('.vc_column-inner', this).css('background-image','none', '!important');				
				after_inlinecss += 'background-image: '+bgimage+';';
			}
			
			/* * Background Color * */
			if( jQuery('.vc_column-inner', this).css('background-color')!='' || jQuery('.vc_column-inner', this).css('background-color')!='inherit' ){
				var bgcolor = jQuery('.vc_column-inner', this).css('background-color');
				before_inlinecss += 'background-color: '+bgcolor+';';
			}
			
			
			// Now adding inline style in HEAD tag
			if( after_inlinecss!='' || before_inlinecss!='' ){
				jQuery( "head" ).append( '<style>.'+randomclass+':after{'+after_inlinecss+'} .'+randomclass+':before{'+before_inlinecss+'} .ts-right-span .vc_column-inner{background-image:none !important;}</style>' );
			}
			
			
			
		}
	});
}


/* Circle progressbar */
function labtechco_circle_progressbar(){
	/**************/
	jQuery('.ts-circle-outer').each(function(){
		
		var this_circle = jQuery(this);
		
		// Circle settings
		var emptyFill_val  = this_circle.data('emptyfill');
		var thickness_val  = this_circle.data('thickness');
		var fill_gradient  = this_circle.data('gradient');
		var fill_val       = this_circle.data('fill');
		var startangle_val = (-Math.PI / 4 * 2);
		
		if( this_circle.closest('.ts-fid').hasClass('ts-fid-boxstyle-style2') ){
			var startangle_val = (-Math.PI / 4 * 1.7);
		}
	
		
		console.log(startangle_val);
		
		
		// Gradient settings
		if( fill_gradient!='' ){
			fill_gradient = fill_gradient.split('|');
			fill_val = {gradient: [ fill_gradient[0], fill_gradient[1] ]};
		}
		
		
		
		
		if( typeof jQuery.fn.circleProgress == "function" ){
			var digit   = this_circle.data('digit');
			var before  = this_circle.data('before');
			var after   = this_circle.data('after');
			var digit       = Number( digit );
			var short_digit = ( digit/100 );
			var size_val	= this_circle.data('size');
			
			jQuery('.ts-circle', this_circle ).circleProgress({
				value: 0,
				size: size_val,
				startAngle: startangle_val,
				thickness: thickness_val,
				emptyFill: emptyFill_val,
				fill: fill_val
			}).on('circle-animation-progress', function(event, progress, stepValue) { // Rotate number when animating
				this_circle.find('.ts-circle-number').html( before + Math.round( stepValue*100 ) + after );
			});
			
		}
		
		
		//this_circle.html('0');
		if(  void 0 !== jQuery.fn.vcwaypoint  ){
			this_circle.vcwaypoint(function(direction) {
				if( !this_circle.hasClass('completed') ){
					
					// Re draw when view
					if( typeof jQuery.fn.circleProgress == "function" ){
						jQuery('.ts-circle', this_circle ).circleProgress( { value: short_digit } );
					};
					
					
					
					this_circle.addClass('completed');
					
				}
				
				
			}, { offset:'85%' });
		
		}

		
		
		
	});
}
	

/******************************/









jQuery( document ).ready(function($) {
	
	"use strict";
	
	
	
	/*------------------------------------------------------------------------------*/
	/* Search form changes for search results page only
	/*------------------------------------------------------------------------------*/
	themestek_search_form();
	
	
	/*------------------------------------------------------------------------------*/
	/* Circle Progressbar
	/*------------------------------------------------------------------------------*/
	labtechco_circle_progressbar();
	
	
	
	jQuery('a[data-rel^="prettyPhoto"]').prettyPhoto();
	jQuery('a.lightboxvid, .lightboxvid a').prettyPhoto();
	jQuery('a[rel^="prettyPhoto"]').prettyPhoto();
	
	/*------------------------------------------------------------------------------*/
	/* Floating Bar code
	/*------------------------------------------------------------------------------*/
	
	themestek_hide_gmap();
	
	// Top btn click event
	jQuery(".themestek-fbar-btn > a.themestek-fbar-btn-link").on('click', function(){		
		if( jQuery(this).closest('.themestek-fbar-main-w').hasClass('themestek-fbar-position-default') ){
			// Fbar top position
			if( jQuery('.themestek-fbar-box-w').css('display')=='none' ){
				jQuery('.ts-fbar-open-icon', this).fadeOut();
				jQuery('.ts-fbar-close-icon', this).fadeIn();
				
				jQuery('.themestek-fbar-box-w').slideDown();
			} else {
				jQuery('.ts-fbar-open-icon', this).fadeIn();
				jQuery('.ts-fbar-close-icon', this).fadeOut();
				
				jQuery('.themestek-fbar-box-w').slideUp();
			}
		} else {
			// Fbar right position
		}		
		
		return false;
	});	
	
	
	// Right btn click event
	jQuery('.ts-fbar-close, .themestek-fbar-btn > a.themestek-fbar-btn-link, .ts-float-overlay').on('click', function(){
		jQuery('.themestek-fbar-box-w').toggleClass('animated');
		jQuery('.ts-float-overlay').toggleClass('animated');
		jQuery('.themestek-fbar-btn').toggleClass('animated');		
	});

	
	
	
	
	
	/*------------------------------------------------------------------------------*/
	/* Add plus icon in menu
	/*------------------------------------------------------------------------------*/ 
	jQuery( "#site-navigation .nav-menu > li.menu-item-has-children, #site-navigation div.nav-menu > ul > li.page_item_has_children, .ts-mmmenu-override-yes #navbar #site-navigation .mega-menu-wrap .mega-menu.mega-menu-horizontal > li.mega-menu-item-has-children" ).append( "<span class='righticon'><i class='tsicon-fa-plus-square'></i></span>" );
	
		
	jQuery('#site-header-menu #site-navigation div.nav-menu > ul > li:has(ul), .ts-mmmenu-override-yes #site-header-menu #site-navigation .mega-menu-wrap > ul > li:has(ul)').append("<span class='righticon'><i class='ts-labtechco-icon-angle-down'></i></span>");	
		
	jQuery('.ts-mmmenu-override-yes #site-navigation .mega-menu-wrap > ul > li.menu-item-language ul').addClass("mega-sub-menu");		
	jQuery('.ts-mmmenu-override-yes #navbar #site-navigation .mega-menu-wrap .mega-menu.mega-menu-horizontal > li.menu-item-language > a').show();
	jQuery('.ts-mmmenu-override-yes #site-navigation .mega-menu-wrap > ul > li.menu-item-language').hover(
         function () {			 		 
		   jQuery('.ts-mmmenu-override-yes #navbar #site-navigation .mega-menu-wrap .mega-menu.mega-menu-horizontal .mega-menu-flyout .mega-sub-menu').css("display", "none");	
           jQuery(this).find('ul').show();		   
         }, 
         function () {
           jQuery(this).find('ul').hide();
         }
     );
	
	
	jQuery('.menu li.current-menu-item').parents('li.mega-menu-megamenu').addClass('mega-current-menu-ancestor');	
	if (!jQuery('body').hasClass("ts-header-invert")) {	
		jQuery( ".nav-menu > li:eq(-2), #site-header-menu #site-navigation div.mega-menu-wrap ul.mega-menu.mega-menu-horizontal > li:eq(-2)" ).addClass( "lastsecond" );
		jQuery( ".nav-menu > li:eq(-1), #site-header-menu #site-navigation div.mega-menu-wrap ul.mega-menu.mega-menu-horizontal > li:eq(-1)" ).addClass( "last" );	
	}
	
	
	/*------------------------------------------------------------------------------*/
	/* Responsive Menu
	/*------------------------------------------------------------------------------*/
	jQuery('.righticon').on('click', function() {
		if(jQuery(this).siblings('.sub-menu, .children, .mega-sub-menu').hasClass('open')){
			jQuery(this).siblings('.sub-menu, .children, .mega-sub-menu').removeClass('open');
			jQuery( 'i', jQuery(this) ).removeClass('ts-labtechco-icon-angle-up').addClass('ts-labtechco-icon-angle-down');
		} else {
			jQuery(this).siblings('.sub-menu, .children, .mega-sub-menu').addClass('open');			
			jQuery( 'i', jQuery(this) ).removeClass('ts-labtechco-icon-angle-down').addClass('ts-labtechco-icon-angle-up');
		}
		return false;
 	});
	
	
	
	
	
	
	
	
	/*------------------------------------------------------------------------------*/
	/* adding prettyPhoto in Gallery
	/*------------------------------------------------------------------------------*/
	jQuery("a[data-gal^='prettyPhoto']").prettyPhoto({hook: 'data-gal'});
	
	
	/*------------------------------------------------------------------------------*/
	/* Revolution Slider - Removing extra margin for no slider message
	/*------------------------------------------------------------------------------*/
	jQuery( ".themestek-slider-wrapper > div > div > div:contains('Revolution Slider Error')" ).css( "margin-top", "0" );
	
	
	
	/*------------------------------------------------------------------------------*/
	/* Select2 library for all SELECT element
	/*------------------------------------------------------------------------------*/
	jQuery('select').select2();
	
	
	
	/*------------------------------------------------------------------------------*/
	/* YITH Wishlist functionality
	/*------------------------------------------------------------------------------*/
	themestek_yith_wishlist_func();
	
	
	/*------------------------------------------------------------------------------*/
	/* Logo Margin Padding
	/*------------------------------------------------------------------------------*/
	labtechco_logMarginPadding();
	labtechco_logMarginPadding_right();
	
	
	
	/*------------------------------------------------------------------------------*/
	/* ROW Equal height : Setting bg image as inline so it will appear in mobile mode
	/*------------------------------------------------------------------------------*/	
	jQuery('.vc_row-o-equal-height, .ts-equalheightdiv').each(function(){
		var thisRow = jQuery(this);
		jQuery('.wpb_column', thisRow).each(function(){
			var thisColumn = jQuery(this);
			if(
				(
					(jQuery('.ts-col-wrapper-bg-layer', thisColumn).length > 0 && ( jQuery('.ts-col-wrapper-bg-layer', thisColumn).css('background-image') != 'none')) || // For main column
					(jQuery('.vc_column-inner', thisColumn).length > 0 && ( jQuery('.vc_column-inner', thisColumn).css('background-image') != 'none'))  // for inner_coumn
				) &&
				(jQuery('.wpb_wrapper', thisColumn).html().trim() == '')
				
			) {
				
				if(jQuery('.ts-col-wrapper-bg-layer', thisColumn).length > 0 && ( jQuery('.ts-col-wrapper-bg-layer', thisColumn).css('background-image') != 'none')){
					var bgimage = jQuery('.ts-col-wrapper-bg-layer', thisColumn).css('background-image').replace('url(','');
					bgimage     = bgimage.replace(')','');		
					
				} else {
					var bgimage = jQuery('.vc_column-inner', thisColumn).css('background-image').replace('url(','');
					bgimage     = bgimage.replace(')','');		
					
				}
				
				if( jQuery('.ts-equal-height-image', thisColumn ).length==0 ){
					jQuery('.vc_column-inner', thisColumn).after('<img src=' + bgimage + ' class="ts-equal-height-image" />');
				}
				
				
				jQuery(thisColumn).addClass('ts-emtydiv');
			}
		});

	});
	
	
	
	
	/*------------------------------------------------------------------------------*/
	/* Header Search Form
	/*------------------------------------------------------------------------------*/
	
	jQuery( ".ts-header-search-link a" ).on('click', function() {			
	  		jQuery(".ts-search-overlay").addClass('st-show');
			jQuery("body").addClass('st-prevent-scroll');			
			jQuery(".field.searchform-s").focus();					    
	 		return false;
	});		
	jQuery( ".ts-icon-close" ).on('click', function() {
	  		jQuery(".ts-search-overlay").removeClass('st-show');
			jQuery("body").removeClass('st-prevent-scroll');					  
	 		return false;
	});	
	jQuery('.ts-site-searchform').on('click', function(event){
		event.stopPropagation();
	});
	

	/*------------------------------------------------------------------------------*/
	/* Social icon
	/*------------------------------------------------------------------------------*/ 
	
	jQuery(".themestek-row-fullwidth-true.full-colum-height-widht > .grid_section > .vc_column_container img.vc_single_image-img").each(function() {  
       var imgsrc = jQuery(this).attr("src");
	   jQuery(this).parent().parent().parent().parent().parent('.vc_column_container').css('background-image', 'url(' + imgsrc + ')');       
  	});	
		
	

	 	
	/*------------------------------------------------------------------------------*/
	/* Applying prettyPhoto to all images
	/*------------------------------------------------------------------------------*/
	if( typeof jQuery.fn.prettyPhoto == "function" ){
		
		
		// Gallery
		jQuery('div.gallery a[href*=".jpg"], div.gallery a[href*=".jpeg"], div.gallery a[href*=".png"], div.gallery a[href*=".gif"]').each(function(){
			if( jQuery(this).attr('target')!='_blank' ){
				jQuery(this).attr('rel','prettyPhoto[wp-gallery]');
			}
		});
		
		// WordPress Gallery
		jQuery('.gallery-item a[href*=".jpg"], .gallery-item a[href*=".jpeg"], .gallery-item a[href*=".png"], .gallery-item a[href*=".gif"]').each(function(){
			if( jQuery(this).attr('target')!='_blank' ){
				jQuery(this).attr('rel','prettyPhoto[coregallery]');
			}
		});
		
		// Normal link
		jQuery('a[href*=".jpg"], a[href*=".jpeg"], a[href*=".png"], a[href*=".gif"]').each(function(){
			if( jQuery(this).attr('target')!='_blank' && !jQuery(this).hasClass('prettyphoto') ){
				var attr = $(this).attr('rel');
				// For some browsers, `attr` is undefined; for others,
				// `attr` is false.  Check for both.
				if (typeof attr !== typeof undefined && attr !== false && attr!='prettyPhoto' ) {
					jQuery(this).attr('data-rel','prettyPhoto');
				}
			}
		});		

		jQuery('a[data-rel^="prettyPhoto"]').prettyPhoto();
		jQuery('a.ts_prettyphoto, div.ts_prettyphoto a').prettyPhoto();
		jQuery('a[rel^="prettyPhoto"]').prettyPhoto();

		
		/*------------------------------------------------------------------------------*/
		/* Settting for lightbox content in Portfolio slider
		/*------------------------------------------------------------------------------*/
		jQuery("a.themestek-open-gallery").on('click', function(){
			var id   = jQuery(this).data('id');
			var currid = window[ 'api_images_' + id ];
			jQuery.prettyPhoto.open( window[ 'api_images_' + id ] , window[ 'api_titles_' + id ] , window[ 'api_desc_' + id ] );
		});
		
	}
		
		
		
		

	/*------------------------------------------------------------------------------*/
	/* Animation on scroll: Number rotator
	/*------------------------------------------------------------------------------*/
	$("[data-appear-animation]").each(function() {
		var self      = $(this);
		var animation = self.data("appear-animation");
		var delay     = (self.data("appear-animation-delay") ? self.data("appear-animation-delay") : 0);
		
		if( $(window).width() > 959 ) {
			self.html('0');
			if(  void 0 !== jQuery.fn.vcwaypoint  ){
				self.vcwaypoint(function(direction) {
					if( !self.hasClass('completed') ){
						var from     = self.data('from');
						var to       = self.data('to');
						var interval = self.data('interval');
						self.numinate({
							format: '%counter%',
							from: from,
							to: to,
							runningInterval: 2000,
							stepUnit: interval,
							onComplete: function(elem) {
								self.addClass('completed');
							}
						});
					}
				}, { offset:'85%' });
			}
		} else {
			if( animation == 'animateWidth' ) {
				self.css('width', self.data("width"));
			}
		}
	});

	/*------------------------------------------------------------------------------*/
	/* Set height of boxes inside row-column view of Blog and Portfolio
	/*------------------------------------------------------------------------------*/
	if( jQuery('.themestek-testimonial-box' ).length > 0 ){
		setHeight('.themestek-testimonial-box.col-lg-6.col-sm-6.col-md-6');
		setHeight('.themestek-testimonial-box.col-lg-4.col-sm-6.col-md-4');
		setHeight('.themestek-testimonial-box.col-lg-3.col-sm-6.col-md-3');
	}
	
	/*------------------------------------------------------------------------------*/
	/* Sticky
	/*------------------------------------------------------------------------------*/
	if( jQuery('.ts-stickable-header').length > 0 ){		

		ts_sticky();
	}	

	/*------------------------------------------------------------------------------*/
	/* Return Fasle when # Url
	/*------------------------------------------------------------------------------*/
	$('#site-navigation a[href="#"]').on('click', function(){return false;});	
	
	
	/*------------------------------------------------------------------------------*/
	/* Welcome bar close button
	/*------------------------------------------------------------------------------*/
	$(".themestek-close-icon").on('click', function(){
		$("#page").css('padding-top', (parseInt($("#page").css('padding-top')) - parseInt($(".themestek-wbar").height()) ) + 'px' );
		$(".themestek-wbar").slideUp();
		themestek_setCookie('ts_hidewbar','1',1);
	});

	/*------------------------------------------------------------------------------*/
	/* Removing BR tag added by shortcode generator
	/*------------------------------------------------------------------------------*/
	var galleryhtml = jQuery(".gallery-size-full br").each(function(){
		jQuery(this).remove();
	});	



	/*------------------------------------------------------------------------------*/
	/* Settting for lightbox content in Blog
	/*------------------------------------------------------------------------------*/
	jQuery("a.themestek-open-gallery").on('click', function(){
		var href   = jQuery(this).attr('href');
		var id     = href.replace("#themestek-embed-code-", "");
		var currid = window[ 'api_images_' + id ];
		jQuery.prettyPhoto.open( window[ 'api_images_' + id ] , window[ 'api_titles_' + id ] , window[ 'api_desc_' + id ] );
	});
	
	
	
	/*-----------------------------------------------------------------------------------*/
	/*	Isotope
	/*-----------------------------------------------------------------------------------*/
	if( jQuery().isotope ){
		jQuery(window).on( 'load', function () {
			"use strict";
			themestek_isotope();	
			//themestek_blogmasonry();		
		});
		jQuery(window).resize(function(){
			themestek_isotope();
		});
	}
	
	
	
	
	
	/*------------------------------------------------------------------------------*/
	/* Setup Post Likes
	/*------------------------------------------------------------------------------*/
	$('.themestek-portfolio-likes').on('click', function(e){
		e.preventDefault();
		var link = $(this);
		if(link.hasClass('like-active')) return false;
		
		$(this).html('<i class="fa fa-circle-o-notch fa fa-spin"></i>');
		
		var id = $(this).attr('id');

		$.post(ajaxurl, {action: 'themestek-portfolio-likes', likes_id: id}, function(data){
			$( 'i.fa fa-heart-o', link ).removeClass('fa fa-heart-o').addClass('fa fa-heart');
			link.html(data).addClass('like-active');
		});
	});
	
	
	/*------------------------------------------------------------------------------*/
	/* Sticky Footer
	/*------------------------------------------------------------------------------*/
	jQuery('footer#colophon').resize(function(){
		themestek_stickyFooter();
	});
	themestek_stickyFooter();	
	


	/*------------------------------------------------------------------------------*/
	/* Equal Height Div load
	/*------------------------------------------------------------------------------*/	
	equalheight('.ts-equalheightdiv  .wpb_column.vc_column_container');
	
	ts_hide_togle_link();
	
	jQuery( "#ts-header-slider > div > div:contains('Revolution Slider Error')" ).css( "margin", "auto" );
	
	/*------------------------------------------------------------------------------*/
	/*  Timeline view
	/*------------------------------------------------------------------------------*/	
	
		$.fn.smTimeline = function( option, value ) {
			jQuery( this ).each( function() {
				var $sm_timeline = jQuery( this );
				
				var is_mobile_view = jQuery( window ).width() < 768;
				$sm_timeline.find( '.timeline-element' ).each( function() {
					var $this = jQuery( this );
					var $timeline_spine = $this.find( '.ts-timeline-spine' );
					if ( is_mobile_view ) {
						$this.addClass( 'wow fadeInUp' );
						$timeline_spine.attr( 'style', '' );
					} else {
						if ( $this.hasClass( 'left-side' ) ) {
							$this.find( '.ts-animation-wrap' ).addClass( 'wow fadeInLeft' );
						} else if ( $this.hasClass( 'right-side' ) ) {
							$this.find( '.ts-animation-wrap' ).addClass( 'wow fadeInRight' );
						}
						
						if ( $this.next().length == 0 ) return;
						var $next = $this.next();
						var $next_tl_spine = $next.find( '.ts-timeline-spine' );
						
						
						
						if ( $next.hasClass( 'ts-date-separator' ) ) {
							$timeline_spine.height( $next.offset().top - $timeline_spine.offset().top - 5 );					
						} else if ( $next_tl_spine.length ) {							
							$timeline_spine.height( $next_tl_spine.offset().top - $timeline_spine.offset().top - 25 );
						} 
					}
				} );
			} );
		}
	
	
	/* ***************** */
	/*  Carousel effect  */
	/* ***************** */

	jQuery('.themestek-boxes-view-carousel, .themestek-boxes-view-carousel-leftimg, .themestek-boxes-view-carousel-bottomimg').each(function(){
		var thisElement = jQuery(this);
		
		
		
		// Column
		var ts_column         = 3;
		var ts_slidestoscroll = 3;
		
		var ts_slidestoscroll_1200 = 3;
		var ts_slidestoscroll_992  = 3;
		var ts_slidestoscroll_768  = 2;
		var ts_slidestoscroll_479  = 1;
		var ts_slidestoscroll_0    = 1;
		if( jQuery(this).data('ts-slidestoscroll')=='1' ){  // slides to scroll
			var ts_slidestoscroll      = 1;
			var ts_slidestoscroll_1200 = 1;
			var ts_slidestoscroll_992  = 1;
			var ts_slidestoscroll_768  = 1;
			var ts_slidestoscroll_479  = 1;
			var ts_slidestoscroll_0    = 1;
		}
		
		
		// responsive
		var ts_responsive = [
			{ breakpoint: 1200, settings: {
				slidesToShow  : 3,
				slidesToScroll: ts_slidestoscroll_1200
			} },
			{ breakpoint: 768, settings: {
				slidesToShow  : 2,
				slidesToScroll: ts_slidestoscroll_768
			} },
			{ breakpoint: 479, settings: {
				slidesToShow  : 1,
				slidesToScroll: ts_slidestoscroll_479
			} },
			{ breakpoint: 0, settings: {
				slidesToShow  : 1,
				slidesToScroll: ts_slidestoscroll_0
			} }
		];
			
		
			
		if( jQuery(this).hasClass('themestek-boxes-col-three') ){
			ts_column         = 3;
			ts_slidestoscroll = 3;
			
			var ts_slidestoscroll_1200 = 3;
			var ts_slidestoscroll_768  = 2;
			var ts_slidestoscroll_479  = 1;
			var ts_slidestoscroll_0    = 1;
			if( jQuery(this).data('ts-slidestoscroll')=='1' ){  // slides to scroll
				var ts_slidestoscroll      = 1;
				var ts_slidestoscroll_1200 = 1;
				var ts_slidestoscroll_768  = 1;
				var ts_slidestoscroll_479  = 1;
				var ts_slidestoscroll_0    = 1;
			}
			
			ts_responsive     = [
				{ breakpoint: 1200, settings: {
					slidesToShow  : 3,
					slidesToScroll: ts_slidestoscroll_1200,
				} },
				{ breakpoint: 768, settings: {
					slidesToShow  : 2,
					slidesToScroll: ts_slidestoscroll_768
				} },
				{ breakpoint: 479, settings: {
					slidesToShow  : 1,
					slidesToScroll: ts_slidestoscroll_479
				} },
				{ breakpoint: 0, settings: {
					slidesToShow  : 1,
					slidesToScroll: ts_slidestoscroll_0
				} }
			];
		
		} else if( jQuery(this).hasClass('themestek-boxes-col-one') ){
		
			ts_column         = 1;
			ts_slidestoscroll = 1;
			
			ts_responsive     = [
				{ breakpoint: 1200, settings: {
					slidesToShow  : 1,
					slidesToScroll: 1,
					arrows: false
				} },
				{ breakpoint: 768, settings: {
					slidesToShow  : 1,
					slidesToScroll: 1,
					arrows: false
				} },
				{ breakpoint: 479, settings: {
					slidesToShow  : 1,
					slidesToScroll: 1,
					arrows: false
				} },
				{ breakpoint: 0, settings: {
					slidesToShow  : 1,
					slidesToScroll: 1,
					arrows: false
				} }
			];
			
		} else if( jQuery(this).hasClass('themestek-boxes-col-two') ){
			ts_column         = 2;
			ts_slidestoscroll = 2;
			
			var ts_slidestoscroll_1200 = 2;
			var ts_slidestoscroll_768  = 2;
			var ts_slidestoscroll_479  = 1;
			var ts_slidestoscroll_0    = 1;
			if( jQuery(this).data('ts-slidestoscroll')=='1' ){  // slides to scroll
				var ts_slidestoscroll      = 1;
				var ts_slidestoscroll_1200 = 1;
				var ts_slidestoscroll_768  = 1;
				var ts_slidestoscroll_479  = 1;
				var ts_slidestoscroll_0    = 1;
			}
			
			ts_responsive     = [
				{ breakpoint: 1200, settings: {
					slidesToShow  : 2,
					slidesToScroll: ts_slidestoscroll_1200
				} },
				{ breakpoint: 768, settings: {
					slidesToShow  : 2,
					slidesToScroll: ts_slidestoscroll_768
				} },
				{ breakpoint: 479, settings: {
					slidesToShow  : 1,
					slidesToScroll: ts_slidestoscroll_479
				} },
				{ breakpoint: 0, settings: {
					slidesToShow  : 1,
					slidesToScroll: ts_slidestoscroll_0
				} }
			];
			
		
		} else if( jQuery(this).hasClass('themestek-boxes-col-four') ){
			ts_column         = 4;
			ts_slidestoscroll = 4;
			
			var ts_slidestoscroll_1200 = 4;
			var ts_slidestoscroll_992  = 3;
			var ts_slidestoscroll_768  = 2;
			var ts_slidestoscroll_479  = 1;
			var ts_slidestoscroll_0    = 1;
			if( jQuery(this).data('ts-slidestoscroll')=='1' ){  // slides to scroll
				var ts_slidestoscroll      = 1;
				var ts_slidestoscroll_1200 = 1;
				var ts_slidestoscroll_992  = 1;
				var ts_slidestoscroll_768  = 1;
				var ts_slidestoscroll_479  = 1;
				var ts_slidestoscroll_0    = 1;
			}
			
			ts_responsive     = [
				{ breakpoint: 1200, settings: {
					slidesToShow  : 4,
					slidesToScroll: ts_slidestoscroll_1200
				} },
				{ breakpoint: 992, settings: {
					slidesToShow  : 3,
					slidesToScroll: ts_slidestoscroll_992
				} },
				{ breakpoint: 768, settings: {
					slidesToShow  : 2,
					slidesToScroll: ts_slidestoscroll_768
				} },
				{ breakpoint: 479, settings: {
					slidesToShow  : 1,
					slidesToScroll: ts_slidestoscroll_479
				} },
				{ breakpoint: 0, settings: {
					slidesToShow  : 1,
					slidesToScroll: ts_slidestoscroll_0
				} }
			];
			
			
		} else if( jQuery(this).hasClass('themestek-boxes-col-five') ){
			ts_column         = 5;
			ts_slidestoscroll = 5;
			
			var ts_slidestoscroll_1200 = 5;
			var ts_slidestoscroll_768  = 3;
			var ts_slidestoscroll_479  = 1;
			var ts_slidestoscroll_0    = 1;
			if( jQuery(this).data('ts-slidestoscroll')=='1' ){  // slides to scroll
				var ts_slidestoscroll      = 1;
				var ts_slidestoscroll_1200 = 1;
				var ts_slidestoscroll_768  = 1;
				var ts_slidestoscroll_479  = 1;
				var ts_slidestoscroll_0    = 1;
			}
			
			ts_responsive     = [
				{ breakpoint: 1200, settings: {
					slidesToShow  : 5,
					slidesToScroll: ts_slidestoscroll_1200
				} },
				{ breakpoint: 768, settings: {
					slidesToShow  : 3,
					slidesToScroll: ts_slidestoscroll_768
				} },
				{ breakpoint: 479, settings: {
					slidesToShow  : 1,
					slidesToScroll: ts_slidestoscroll_479
				} },
				{ breakpoint: 0, settings: {
					slidesToShow  : 1,
					slidesToScroll: ts_slidestoscroll_0
				} }
			];
			
		} else if( jQuery(this).hasClass('themestek-boxes-col-six') ){
			ts_column         = 6;
			ts_slidestoscroll = 6;
			
			var ts_slidestoscroll_1200 = 6;
			var ts_slidestoscroll_768  = 3;
			var ts_slidestoscroll_479  = 1;
			var ts_slidestoscroll_0    = 1;
			if( jQuery(this).data('ts-slidestoscroll')=='1' ){  // slides to scroll
				var ts_slidestoscroll      = 1;
				var ts_slidestoscroll_1200 = 1;
				var ts_slidestoscroll_768  = 1;
				var ts_slidestoscroll_479  = 1;
				var ts_slidestoscroll_0    = 1;
			}
			
			ts_responsive     = [
				{ breakpoint: 1200, settings: {
					slidesToShow  : 6,
					slidesToScroll: ts_slidestoscroll_1200
				} },
				{ breakpoint: 768, settings: {
					slidesToShow  : 3,
					slidesToScroll: ts_slidestoscroll_768
				} },
				{ breakpoint: 479, settings: {
					slidesToShow  : 1,
					slidesToScroll: ts_slidestoscroll_479
				} },
				{ breakpoint: 0, settings: {
					slidesToShow  : 1,
					slidesToScroll: ts_slidestoscroll_0
				} }
			];
		}		
		
		
		// Fade effect
		var ts_fade = false;
		if( jQuery(this).data('ts-effecttype')=='fade' ){
			ts_fade = true;
		}
		

		// Transaction Speed
		var ts_speed = 800;
		if( jQuery.trim( jQuery(this).data('ts-speed') ) != '' ){
			ts_speed = jQuery.trim( jQuery(this).data('ts-speed') );
		}
		
		// Autoplay
		var ts_autoplay = false;
		if( jQuery(this).data('ts-autoplay')=='1' ){
			ts_autoplay = true;
		}
		
		// Autoplay Speed
		var ts_autoplayspeed = 2000;
		if( jQuery.trim( jQuery(this).data('ts-autoplayspeed') ) != '' ){
			ts_autoplayspeed = jQuery.trim( jQuery(this).data('ts-autoplayspeed') );
		}
		
		// Loop
		var ts_loop = false;
		if( jQuery.trim( jQuery(this).data('ts-loop') ) == '1' ){
			ts_loop = true;
		}
		
		// Dots
		var ts_dots = false;
		if( jQuery.trim( jQuery(this).data('ts-dots') ) == '1' ){
			ts_dots = true;
		}
		
		// Next / Prev navigation
		var ts_nav = false;
		if( jQuery.trim( jQuery(this).data('ts-nav') ) == '1' || jQuery.trim( jQuery(this).data('ts-nav') ) == 'above' || jQuery.trim( jQuery(this).data('ts-nav') ) == 'below' ){
			ts_nav = true;
		}
		
		// Center mode
		var ts_centermode = false;
		if( jQuery.trim( jQuery(this).data('ts-centermode') ) == '1' ){
			ts_centermode = true;
		}
		
		// Pause on Focus
		var ts_pauseonfocus = false;
		if( jQuery.trim( jQuery(this).data('ts-pauseonfocus') ) == '1' ){
			ts_pauseonfocus = true;
		}
		
		// Pause on Hover
		var ts_pauseonhover = false;
		if( jQuery.trim( jQuery(this).data('ts-pauseonhover') ) == '1' ){
			ts_pauseonhover = true;
		}
		
		
		// RTL
		var ts_rtl = false;
		if( jQuery('body').hasClass('rtl') ){
			ts_rtl = true;
		}
		
		
		
		
		jQuery('.themestek-boxes-row-wrapper > div', this).removeClass (function (index, css) {
			return (css.match (/(^|\s)col-\S+/g) || []).join(' ');
		});
	
		jQuery('.themestek-boxes-row-wrapper', this).slick({
			fade             : ts_fade,
			speed            : ts_speed,
			centerMode       : ts_centermode,
			pauseOnFocus     : ts_pauseonfocus,
			pauseOnHover     : ts_pauseonhover,
			slidesToShow     : ts_column,
			slidesToScroll   : ts_slidestoscroll,
			autoplay         : ts_autoplay,
			autoplaySpeed    : ts_autoplayspeed,
			rtl              : ts_rtl,
			dots             : ts_dots,
			pauseOnDotsHover : false,
			arrows           : ts_nav,
			adaptiveHeight   : false,
			infinite         : ts_loop,
			responsive       : ts_responsive
  
		});
	});
	
	
	// On resize.. it will re-arrange the Flexslider
	jQuery('.themestek-boxes-row-wrapper', this).on('setPosition', function(event, slick){
		jQuery( this ).find( ".ts-flexslider" ).each(function(){
			jQuery(this).resize();
		});
	});
	
	
	
	
	
	// Next button in heading area
	jQuery(".ts-slick-arrow.ts-slick-next", this ).on('click', function(){
		jQuery('.themestek-boxes-row-wrapper', jQuery(this).closest('.themestek-boxes-view-carousel') ).slick('slickNext');
	});
	
	// Pre button in heading area
	jQuery(".ts-slick-arrow.ts-slick-prev", this).on('click', function(){
		jQuery('.themestek-boxes-row-wrapper', jQuery(this).closest('.themestek-boxes-view-carousel') ).slick('slickPrev');
	});	
	
	
	
	// Testimonials Slick view
	jQuery('.themestek-boxes-view-slickview,.themestek-boxes-view-slickview-leftimg').each(function(){

		// Fade effect
		var ts_fade = false;
		if( jQuery(this).data('ts-effecttype')=='fade' ){
			ts_fade = true;
		}
		
		// Transaction Speed
		var ts_speed = 800;
		if( jQuery.trim( jQuery(this).data('ts-speed') ) != '' ){
			ts_speed = jQuery.trim( jQuery(this).data('ts-speed') );
		}
		
		// Autoplay
		var ts_autoplay = false;
		if( jQuery(this).data('ts-autoplay')=='1' ){
			ts_autoplay = true;
		}
		
		// Autoplay Speed
		var ts_autoplayspeed = 2000;
		if( jQuery.trim( jQuery(this).data('ts-autoplayspeed') ) != '' ){
			ts_autoplayspeed = jQuery.trim( jQuery(this).data('ts-autoplayspeed') );
		}
		
		// Loop
		var ts_loop = false;
		if( jQuery.trim( jQuery(this).data('ts-loop') ) == '1' ){
			ts_loop = true;
		}
		
		// Dots
		var ts_dots = false;
		if( jQuery.trim( jQuery(this).data('ts-dots') ) == '1' ){
			ts_dots = true;
		}
		
		// Next / Prev navigation
		var ts_nav = false;
		if( jQuery.trim( jQuery(this).data('ts-nav') ) == '1' ){
			ts_nav = true;
		}
		
	
		var testinav 	= jQuery('.testimonials-nav', this);
		var testiinfo 	= jQuery('.testimonials-info', this);
		
		/* Options for "Owl Carousel 2"
		 * http://owlcarousel.owlgraphic.com/index.html
		 */
		var rtloption = false;
		if( jQuery('body').hasClass('rtl') ){
			rtloption = true;
		}
		
		// Info
		jQuery('.testimonials-info', this).slick({
			fade			: ts_fade,
			//arrows			: ts_nav,
			arrows			: true,
			asNavFor		: testinav,
			adaptiveHeight	: true,
			speed			: ts_speed,
			autoplay		: ts_autoplay,
			autoplaySpeed	: ts_autoplayspeed,
			infinite		: ts_loop,
			rtl             : rtloption
		});
		// Navigation
	   jQuery('.testimonials-nav', this).slick({
			slidesToShow	: 1,
			asNavFor		: testiinfo,
			centerMode		: true,
			centerPadding	: 0,
			focusOnSelect	: true,
			autoplay		: ts_autoplay,
			autoplaySpeed	: ts_autoplayspeed,
			speed			: ts_speed,
			arrows			: ts_nav,
			//arrows			: true,
			dots			: ts_dots,
			variableWidth	: true,
			infinite		: ts_loop,
			rtl             : rtloption
		});
	});
	
	


	// Testimonials Slick view
	jQuery('.themestek-boxes-view-slickview-bottomimg').each(function(){

		// Fade effect
		var ts_fade = false;
		if( jQuery(this).data('ts-effecttype')=='fade' ){
			ts_fade = true;
		}
		
		// Transaction Speed
		var ts_speed = 800;
		if( jQuery.trim( jQuery(this).data('ts-speed') ) != '' ){
			ts_speed = jQuery.trim( jQuery(this).data('ts-speed') );
		}
		
		// Autoplay
		var ts_autoplay = false;
		if( jQuery(this).data('ts-autoplay')=='1' ){
			ts_autoplay = true;
		}
		
		// Autoplay Speed
		var ts_autoplayspeed = 2000;
		if( jQuery.trim( jQuery(this).data('ts-autoplayspeed') ) != '' ){
			ts_autoplayspeed = jQuery.trim( jQuery(this).data('ts-autoplayspeed') );
		}
		
		// Loop
		var ts_loop = false;
		if( jQuery.trim( jQuery(this).data('ts-loop') ) == '1' ){
			ts_loop = true;
		}
		
		// Dots
		var ts_dots = false;
		if( jQuery.trim( jQuery(this).data('ts-dots') ) == '1' ){
			ts_dots = true;
		}
		
		// Next / Prev navigation
		var ts_nav = false;
		if( jQuery.trim( jQuery(this).data('ts-nav') ) == '1' ){
			ts_nav = true;
		}
		
	
		var testinav 	= jQuery('.testimonials-nav', this);
		var testiinfo 	= jQuery('.testimonials-info', this);
		
		/* Options for "Owl Carousel 2"
		 * http://owlcarousel.owlgraphic.com/index.html
		 */
		var rtloption = false;
		if( jQuery('body').hasClass('rtl') ){
			rtloption = true;
		}
		
		// Info
		jQuery('.testimonials-info', this).slick({
			fade			: ts_fade,
			//arrows			: ts_nav,
			arrows			: false,
			asNavFor		: testinav,
			adaptiveHeight	: true,
			speed			: ts_speed,
			autoplay		: ts_autoplay,
			autoplaySpeed	: ts_autoplayspeed,
			infinite		: ts_loop,
			rtl             : rtloption
		});
		// Navigation
	   jQuery('.testimonials-nav', this).slick({
			slidesToShow	: 1,
			asNavFor		: testiinfo,
			centerMode		: true,
			centerPadding	: 0,
			focusOnSelect	: true,
			autoplay		: ts_autoplay,
			autoplaySpeed	: ts_autoplayspeed,
			speed			: ts_speed,
			//arrows			: ts_nav,
			arrows			: true,
			dots			: ts_dots,
			variableWidth	: true,
			infinite		: ts_loop,
			rtl             : rtloption
		});
	});
	

	
	/*------------------------------------------------------------------------------*/
	/* One Page setting
	/*------------------------------------------------------------------------------*/	
	if( jQuery('body').hasClass('themestek-one-page-site') ){
		
		
		// Applying active class to home link
		var x = 1;
		nav = jQuery('.mega-menu-wrap, div.nav-menu');
		nav.find('a[href="#ts-home"]').parent().addClass('mega-current-menu-item mega-current_page_item current-menu-ancestor current-menu-item current_page_item');
		nav.find('a').each(function(){
			if( x != 1 ){
				jQuery(this).parent().removeClass('mega-current-menu-item mega-current_page_item current-menu-ancestor current-menu-item current_page_item');
			}
			x = 0;
		});
		
		
		
		var sections = jQuery('.ts-row, #ts-header-slider'),
		nav          = jQuery('.mega-menu-wrap, div.nav-menu'),
		nav_height   = jQuery('#site-navigation').data('sticky-height')-1;
		
		jQuery(window).on('scroll', function () {
			
			// active first menu
			if( jQuery('body').scrollTop() < 5 ){
				nav.find('a').parent().removeClass('mega-current-menu-item mega-current_page_item current-menu-ancestor current-menu-item current_page_item');						
				nav.find('a[href="#ts-home"]').parent().addClass('mega-current-menu-item mega-current_page_item current-menu-ancestor current-menu-item current_page_item');
			}			
				
				var cur_pos = jQuery(this).scrollTop(); 
				sections.each(function() {
					
					var top = jQuery(this).offset().top - (nav_height+2),
					bottom = top + jQuery(this).outerHeight(); 
		
					if (cur_pos >= top && cur_pos <= bottom) {
						
						
		
						if( typeof jQuery(this) != 'undefined' && typeof jQuery(this).attr('id')!='undefined' && jQuery(this).attr('id')!='' ){
							
							var mainThis = jQuery(this);							
							nav.find('a').removeClass('mega-current-menu-item mega-current_page_item current-menu-ancestor current-menu-item current_page_item');						
							jQuery(this).addClass('mega-current-menu-item mega-current_page_item current-menu-ancestor current-menu-item current_page_item');
							var arr = mainThis.attr('id');							
							
							// Applying active class
							nav.find('a').parent().removeClass('mega-current-menu-item mega-current_page_item current-menu-ancestor current-menu-item current_page_item');
							nav.find('a').each(function(){
								var menuAttr = jQuery(this).attr('href').split('#')[1];						
								if( menuAttr == arr ){
									jQuery(this).parent().addClass('mega-current-menu-item mega-current_page_item current-menu-ancestor current-menu-item current_page_item');
								}
							})
						
						}
					}
				});
			//}
		});
		
		nav.find('a').on('click', function () {
			var $el = jQuery(this), 
			id = $el.attr('href');
			var arr=id.split('#')[1];	  
			jQuery('html, body').animate({
				scrollTop: jQuery('#'+ arr).offset().top - nav_height
			}, 500);  
			return false;
		});
		
	}


	
	
	
} ); // END of  document.ready








jQuery(window).on( 'load', function(){

	"use strict";
	
	
	
	/*------------------------------------------------------------------------------*/
	/* Flex Slider
	/*------------------------------------------------------------------------------*/
	if( jQuery('.ts-flexslider').length > 0 ){
		jQuery('.ts-flexslider').flexslider({
			animation   : "slide",
			controlNav  : true,			
			directionNav: false,
			start: function(){				
				if ( jQuery( '.ts-timeline' ).length > 0 ) { jQuery( '.ts-timeline' ).smTimeline(); }
			}
		});
	}
	
	
	/*------------------------------------------------------------------------------*/
	/* Hide pre-loader
	/*------------------------------------------------------------------------------*/
	function themestek_hide_preloader(){ jQuery( '.ts-pre-loader-container' ).fadeOut( 1000 ); }
	if ( jQuery( '.ts-pre-loader-container' ).length > 0 ) {
		setTimeout(themestek_hide_preloader, 100);
	}
	
	
	
	// Timeline view function
	if ( jQuery( '.ts-timeline' ).length > 0 ) {
		jQuery( '.ts-timeline' ).smTimeline();
	}
	
	
	
	
	
	/*------------------------------------------------------------------------------*/
	/* IsoTope
	/*------------------------------------------------------------------------------*/
	var $container = jQuery('.portfolio-wrapper');
	$container.isotope({
		filter: '*',
		animationOptions: {
			duration: 750,
			easing: 'linear',
			queue: false,
		}
	});
	jQuery('nav.portfolio-sortable-list ul li a').on('click', function(){
		var selector = jQuery(this).attr('data-filter');
		$container.isotope({
			filter: selector,
			animationOptions: {
				duration: 750,
				easing: 'linear',
				queue: false,
			}
		});
		// Selected class
		jQuery('nav.portfolio-sortable-list').find('a.selected').removeClass('selected');
		jQuery(this).addClass('selected'); 
		return false;
	});
	
	
	
	
	/*------------------------------------------------------------------------------*/
	/* Nivo Slider
	/*------------------------------------------------------------------------------*/
	if( jQuery('.themestek-slider-wrapper .nivoSlider').length>0 ){
		jQuery('.themestek-slider-wrapper .nivoSlider').nivoSlider();
	}
	
	
	
	
	
	/* Options for "Owl Carousel 2"
	 * http://owlcarousel.owlgraphic.com/index.html
	 */
	var rtloption = false;
	if( jQuery('body').hasClass('rtl') ){
		rtloption = true;
	}
	
	jQuery('.ts-slick-carousel').slick({
		autoplay: true,
		arrows  : false,
		dots    : true,
		rtl     : rtloption,
	});
	
	


	 
	/*------------------------------------------------------------------------------*/
	/* Enables menu toggle for small screens.
	/*------------------------------------------------------------------------------*/ 
	 
	( function() {
		var nav = jQuery( '#site-navigation' ), button, menu;
		if ( ! nav )
			return;

		button = nav.find( '.menu-toggle' );
		if ( ! button )
			return;

		// Hide button if menu is missing or empty.
		menu = nav.find( '.nav-menu' );
		if ( ! menu || ! menu.children().length ) {
			button.hide();
			return;
		}

		jQuery( '.menu-toggle' ).on( 'click.labtechco', function() {
			nav.toggleClass( 'toggled-on' );
		} );
	} )();
	
	
	
	
	

	
	
	
	/*------------------------------------------------------------------------------*/
	/* Responsive Menu : Open by clicking on the menu text too
	/*------------------------------------------------------------------------------*/
	jQuery('.righticon').each(function() {
		var mainele = this;
		if( jQuery( mainele ).prev().prev().length > 0 ){
			if( jQuery( mainele ).prev().prev().attr('href')=='#' ){
				jQuery( mainele ).prev().prev().on('click', function(){
					jQuery( mainele ).trigger( "click" );
				});
			}
		}
	});
	
	
	
	/*------------------------------------------------------------------------------*/
	/* Blog masonry view for 2, 3 and 4 columns
	/*------------------------------------------------------------------------------*/
	themestek_blogmasonry();	

		jQuery(".themestek-fbar-content-wrapper").perfectScrollbar({
			suppressScrollX:true,
			includePadding:true
		});
		
		jQuery(".ts-header-style-classic-vertical .ts-header-block").perfectScrollbar({
			suppressScrollX:true,
			includePadding:true
		});

}); // END of window.load




jQuery(window).resize(function() {
	
	"use strict";
	
	/*------------------------------------------------------------------------------*/
	/* Equal Height Div load
	/*------------------------------------------------------------------------------*/	
	equalheight('.ts-equalheightdiv  .wpb_column.vc_column_container');
	
	
	/*------------------------------------------------------------------------------*/
	/*  Timeline view
	/*------------------------------------------------------------------------------*/	
	
	setTimeout(function() {
		jQuery( '.ts-timeline' ).smTimeline();
	}, 100);
	
	
	/*------------------------------------------------------------------------------*/
	/* onResize: Set height of boxes inside row-column view of Blog and Portfolio
	/*------------------------------------------------------------------------------*/
	if( jQuery('.themestek-testimonial-box' ).length > 0 ){
		setHeight('.themestek-testimonial-box.col-lg-4.col-sm-6.col-md-4');
		setHeight('.themestek-testimonial-box.col-lg-6.col-sm-6.col-md-6');
		setHeight('.themestek-testimonial-box.col-lg-3.col-sm-6.col-md-3');
	}
	
	/*------------------------------------------------------------------------------*/
	/* Call header sticky function
	/*------------------------------------------------------------------------------*/
	ts_sticky();
		
	
});  // END of window.resize
