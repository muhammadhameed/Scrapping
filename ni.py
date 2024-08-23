import re
import pandas as pd
import requests
from bs4 import BeautifulSoup
pattern = r"https://www\.nupco\.com/[^\"\s]+"

# Find all matches
text = """

<!doctype html>
		<html dir="rtl" lang="ar">
		
	<head>

				<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<link rel="profile" href="http://gmpg.org/xfn/11">
				<meta http-equiv="X-UA-Compatible" content="IE=edge" />
		<!-- Google Tag Manager --><script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-5MVWVFQ');</script><!-- End Google Tag Manager -->
    <script src="https://wchat.freshchat.com/js/widget.js">
		<style>
            .fc_frame {
                left: 15px !important;
                right: initial !important;
            }
        </style>

		<title>المنافسات &#8211; nupco</title>
					<style type="text/css" id="cst_font_data">
						@font-face {
	font-family: 'CoHeadlineW23-ArabicBold';
	font-weight: 100;
	font-display: auto;
	src: url('https://www.nupco.com/wp-content/uploads/2023/03/CoHeadlineTrial-Bold.ttf') format('truetype');
}
@font-face {
	font-family: 'CoHeadlineW23-ArabicRegular';
	font-weight: 100;
	font-display: auto;
	src: url('https://www.nupco.com/wp-content/uploads/2023/03/CoHeadlineTrial-Regular.ttf') format('truetype');
}
@font-face {
	font-family: 'CoHeadlineW23-ArabicRegular';
	font-weight: 100;
	font-display: auto;
}					</style>
				<meta name='robots' content='max-image-preview:large' />
<link rel="alternate" hreflang="ar" href="https://www.nupco.com/%d8%a7%d9%84%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a7%d8%aa/" />
<link rel="alternate" type="application/rss+xml" title="nupco &laquo; الخلاصة" href="https://www.nupco.com/feed/" />
<link rel="alternate" type="application/rss+xml" title="nupco &laquo; خلاصة التعليقات" href="https://www.nupco.com/comments/feed/" />
<script type="text/javascript">
/* <![CDATA[ */
window._wpemojiSettings = {"baseUrl":"https:\/\/s.w.org\/images\/core\/emoji\/15.0.3\/72x72\/","ext":".png","svgUrl":"https:\/\/s.w.org\/images\/core\/emoji\/15.0.3\/svg\/","svgExt":".svg","source":{"concatemoji":"https:\/\/www.nupco.com\/wp-includes\/js\/wp-emoji-release.min.js?ver=6.5.3"}};
/*! This file is auto-generated */
!function(i,n){var o,s,e;function c(e){try{var t={supportTests:e,timestamp:(new Date).valueOf()};sessionStorage.setItem(o,JSON.stringify(t))}catch(e){}}function p(e,t,n){e.clearRect(0,0,e.canvas.width,e.canvas.height),e.fillText(t,0,0);var t=new Uint32Array(e.getImageData(0,0,e.canvas.width,e.canvas.height).data),r=(e.clearRect(0,0,e.canvas.width,e.canvas.height),e.fillText(n,0,0),new Uint32Array(e.getImageData(0,0,e.canvas.width,e.canvas.height).data));return t.every(function(e,t){return e===r[t]})}function u(e,t,n){switch(t){case"flag":return n(e,"\ud83c\udff3\ufe0f\u200d\u26a7\ufe0f","\ud83c\udff3\ufe0f\u200b\u26a7\ufe0f")?!1:!n(e,"\ud83c\uddfa\ud83c\uddf3","\ud83c\uddfa\u200b\ud83c\uddf3")&&!n(e,"\ud83c\udff4\udb40\udc67\udb40\udc62\udb40\udc65\udb40\udc6e\udb40\udc67\udb40\udc7f","\ud83c\udff4\u200b\udb40\udc67\u200b\udb40\udc62\u200b\udb40\udc65\u200b\udb40\udc6e\u200b\udb40\udc67\u200b\udb40\udc7f");case"emoji":return!n(e,"\ud83d\udc26\u200d\u2b1b","\ud83d\udc26\u200b\u2b1b")}return!1}function f(e,t,n){var r="undefined"!=typeof WorkerGlobalScope&&self instanceof WorkerGlobalScope?new OffscreenCanvas(300,150):i.createElement("canvas"),a=r.getContext("2d",{willReadFrequently:!0}),o=(a.textBaseline="top",a.font="600 32px Arial",{});return e.forEach(function(e){o[e]=t(a,e,n)}),o}function t(e){var t=i.createElement("script");t.src=e,t.defer=!0,i.head.appendChild(t)}"undefined"!=typeof Promise&&(o="wpEmojiSettingsSupports",s=["flag","emoji"],n.supports={everything:!0,everythingExceptFlag:!0},e=new Promise(function(e){i.addEventListener("DOMContentLoaded",e,{once:!0})}),new Promise(function(t){var n=function(){try{var e=JSON.parse(sessionStorage.getItem(o));if("object"==typeof e&&"number"==typeof e.timestamp&&(new Date).valueOf()<e.timestamp+604800&&"object"==typeof e.supportTests)return e.supportTests}catch(e){}return null}();if(!n){if("undefined"!=typeof Worker&&"undefined"!=typeof OffscreenCanvas&&"undefined"!=typeof URL&&URL.createObjectURL&&"undefined"!=typeof Blob)try{var e="postMessage("+f.toString()+"("+[JSON.stringify(s),u.toString(),p.toString()].join(",")+"));",r=new Blob([e],{type:"text/javascript"}),a=new Worker(URL.createObjectURL(r),{name:"wpTestEmojiSupports"});return void(a.onmessage=function(e){c(n=e.data),a.terminate(),t(n)})}catch(e){}c(n=f(s,u,p))}t(n)}).then(function(e){for(var t in e)n.supports[t]=e[t],n.supports.everything=n.supports.everything&&n.supports[t],"flag"!==t&&(n.supports.everythingExceptFlag=n.supports.everythingExceptFlag&&n.supports[t]);n.supports.everythingExceptFlag=n.supports.everythingExceptFlag&&!n.supports.flag,n.DOMReady=!1,n.readyCallback=function(){n.DOMReady=!0}}).then(function(){return e}).then(function(){var e;n.supports.everything||(n.readyCallback(),(e=n.source||{}).concatemoji?t(e.concatemoji):e.wpemoji&&e.twemoji&&(t(e.twemoji),t(e.wpemoji)))}))}((window,document),window._wpemojiSettings);
/* ]]> */
</script>
<style id='wp-emoji-styles-inline-css' type='text/css'>

	img.wp-smiley, img.emoji {
		display: inline !important;
		border: none !important;
		box-shadow: none !important;
		height: 1em !important;
		width: 1em !important;
		margin: 0 0.07em !important;
		vertical-align: -0.1em !important;
		background: none !important;
		padding: 0 !important;
	}
</style>
<link rel='stylesheet' id='wp-block-library-rtl-css' href='https://www.nupco.com/wp-includes/css/dist/block-library/style-rtl.min.css?ver=6.5.3' type='text/css' media='all' />
<style id='classic-theme-styles-inline-css' type='text/css'>
/*! This file is auto-generated */
.wp-block-button__link{color:#fff;background-color:#32373c;border-radius:9999px;box-shadow:none;text-decoration:none;padding:calc(.667em + 2px) calc(1.333em + 2px);font-size:1.125em}.wp-block-file__button{background:#32373c;color:#fff;text-decoration:none}
</style>
<style id='global-styles-inline-css' type='text/css'>
body{--wp--preset--color--black: #000000;--wp--preset--color--cyan-bluish-gray: #abb8c3;--wp--preset--color--white: #ffffff;--wp--preset--color--pale-pink: #f78da7;--wp--preset--color--vivid-red: #cf2e2e;--wp--preset--color--luminous-vivid-orange: #ff6900;--wp--preset--color--luminous-vivid-amber: #fcb900;--wp--preset--color--light-green-cyan: #7bdcb5;--wp--preset--color--vivid-green-cyan: #00d084;--wp--preset--color--pale-cyan-blue: #8ed1fc;--wp--preset--color--vivid-cyan-blue: #0693e3;--wp--preset--color--vivid-purple: #9b51e0;--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple: linear-gradient(135deg,rgba(6,147,227,1) 0%,rgb(155,81,224) 100%);--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan: linear-gradient(135deg,rgb(122,220,180) 0%,rgb(0,208,130) 100%);--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange: linear-gradient(135deg,rgba(252,185,0,1) 0%,rgba(255,105,0,1) 100%);--wp--preset--gradient--luminous-vivid-orange-to-vivid-red: linear-gradient(135deg,rgba(255,105,0,1) 0%,rgb(207,46,46) 100%);--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray: linear-gradient(135deg,rgb(238,238,238) 0%,rgb(169,184,195) 100%);--wp--preset--gradient--cool-to-warm-spectrum: linear-gradient(135deg,rgb(74,234,220) 0%,rgb(151,120,209) 20%,rgb(207,42,186) 40%,rgb(238,44,130) 60%,rgb(251,105,98) 80%,rgb(254,248,76) 100%);--wp--preset--gradient--blush-light-purple: linear-gradient(135deg,rgb(255,206,236) 0%,rgb(152,150,240) 100%);--wp--preset--gradient--blush-bordeaux: linear-gradient(135deg,rgb(254,205,165) 0%,rgb(254,45,45) 50%,rgb(107,0,62) 100%);--wp--preset--gradient--luminous-dusk: linear-gradient(135deg,rgb(255,203,112) 0%,rgb(199,81,192) 50%,rgb(65,88,208) 100%);--wp--preset--gradient--pale-ocean: linear-gradient(135deg,rgb(255,245,203) 0%,rgb(182,227,212) 50%,rgb(51,167,181) 100%);--wp--preset--gradient--electric-grass: linear-gradient(135deg,rgb(202,248,128) 0%,rgb(113,206,126) 100%);--wp--preset--gradient--midnight: linear-gradient(135deg,rgb(2,3,129) 0%,rgb(40,116,252) 100%);--wp--preset--font-size--small: 13px;--wp--preset--font-size--medium: 20px;--wp--preset--font-size--large: 36px;--wp--preset--font-size--x-large: 42px;--wp--preset--spacing--20: 0.44rem;--wp--preset--spacing--30: 0.67rem;--wp--preset--spacing--40: 1rem;--wp--preset--spacing--50: 1.5rem;--wp--preset--spacing--60: 2.25rem;--wp--preset--spacing--70: 3.38rem;--wp--preset--spacing--80: 5.06rem;--wp--preset--shadow--natural: 6px 6px 9px rgba(0, 0, 0, 0.2);--wp--preset--shadow--deep: 12px 12px 50px rgba(0, 0, 0, 0.4);--wp--preset--shadow--sharp: 6px 6px 0px rgba(0, 0, 0, 0.2);--wp--preset--shadow--outlined: 6px 6px 0px -3px rgba(255, 255, 255, 1), 6px 6px rgba(0, 0, 0, 1);--wp--preset--shadow--crisp: 6px 6px 0px rgba(0, 0, 0, 1);}:where(.is-layout-flex){gap: 0.5em;}:where(.is-layout-grid){gap: 0.5em;}body .is-layout-flex{display: flex;}body .is-layout-flex{flex-wrap: wrap;align-items: center;}body .is-layout-flex > *{margin: 0;}body .is-layout-grid{display: grid;}body .is-layout-grid > *{margin: 0;}:where(.wp-block-columns.is-layout-flex){gap: 2em;}:where(.wp-block-columns.is-layout-grid){gap: 2em;}:where(.wp-block-post-template.is-layout-flex){gap: 1.25em;}:where(.wp-block-post-template.is-layout-grid){gap: 1.25em;}.has-black-color{color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-color{color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-color{color: var(--wp--preset--color--white) !important;}.has-pale-pink-color{color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-color{color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-color{color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-color{color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-color{color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-color{color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-color{color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-color{color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-color{color: var(--wp--preset--color--vivid-purple) !important;}.has-black-background-color{background-color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-background-color{background-color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-background-color{background-color: var(--wp--preset--color--white) !important;}.has-pale-pink-background-color{background-color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-background-color{background-color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-background-color{background-color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-background-color{background-color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-background-color{background-color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-background-color{background-color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-background-color{background-color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-background-color{background-color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-background-color{background-color: var(--wp--preset--color--vivid-purple) !important;}.has-black-border-color{border-color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-border-color{border-color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-border-color{border-color: var(--wp--preset--color--white) !important;}.has-pale-pink-border-color{border-color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-border-color{border-color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-border-color{border-color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-border-color{border-color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-border-color{border-color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-border-color{border-color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-border-color{border-color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-border-color{border-color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-border-color{border-color: var(--wp--preset--color--vivid-purple) !important;}.has-vivid-cyan-blue-to-vivid-purple-gradient-background{background: var(--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple) !important;}.has-light-green-cyan-to-vivid-green-cyan-gradient-background{background: var(--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan) !important;}.has-luminous-vivid-amber-to-luminous-vivid-orange-gradient-background{background: var(--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange) !important;}.has-luminous-vivid-orange-to-vivid-red-gradient-background{background: var(--wp--preset--gradient--luminous-vivid-orange-to-vivid-red) !important;}.has-very-light-gray-to-cyan-bluish-gray-gradient-background{background: var(--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray) !important;}.has-cool-to-warm-spectrum-gradient-background{background: var(--wp--preset--gradient--cool-to-warm-spectrum) !important;}.has-blush-light-purple-gradient-background{background: var(--wp--preset--gradient--blush-light-purple) !important;}.has-blush-bordeaux-gradient-background{background: var(--wp--preset--gradient--blush-bordeaux) !important;}.has-luminous-dusk-gradient-background{background: var(--wp--preset--gradient--luminous-dusk) !important;}.has-pale-ocean-gradient-background{background: var(--wp--preset--gradient--pale-ocean) !important;}.has-electric-grass-gradient-background{background: var(--wp--preset--gradient--electric-grass) !important;}.has-midnight-gradient-background{background: var(--wp--preset--gradient--midnight) !important;}.has-small-font-size{font-size: var(--wp--preset--font-size--small) !important;}.has-medium-font-size{font-size: var(--wp--preset--font-size--medium) !important;}.has-large-font-size{font-size: var(--wp--preset--font-size--large) !important;}.has-x-large-font-size{font-size: var(--wp--preset--font-size--x-large) !important;}
.wp-block-navigation a:where(:not(.wp-element-button)){color: inherit;}
:where(.wp-block-post-template.is-layout-flex){gap: 1.25em;}:where(.wp-block-post-template.is-layout-grid){gap: 1.25em;}
:where(.wp-block-columns.is-layout-flex){gap: 2em;}:where(.wp-block-columns.is-layout-grid){gap: 2em;}
.wp-block-pullquote{font-size: 1.5em;line-height: 1.6;}
</style>
<link rel='stylesheet' id='contact-form-7-css' href='https://www.nupco.com/wp-content/plugins/contact-form-7/includes/css/styles.css?ver=5.1.6' type='text/css' media='all' />
<style id='contact-form-7-inline-css' type='text/css'>
.wpcf7 .wpcf7-recaptcha iframe {margin-bottom: 0;}.wpcf7 .wpcf7-recaptcha[data-align="center"] > div {margin: 0 auto;}.wpcf7 .wpcf7-recaptcha[data-align="right"] > div {margin: 0 0 0 auto;}
</style>
<link rel='stylesheet' id='cf7msm_styles-css' href='https://www.nupco.com/wp-content/plugins/contact-form-7-multi-step-module/resources/cf7msm.css?ver=4.4' type='text/css' media='all' />
<link rel='stylesheet' id='contact-form-7-rtl-css' href='https://www.nupco.com/wp-content/plugins/contact-form-7/includes/css/styles-rtl.css?ver=5.1.6' type='text/css' media='all' />
<link rel='stylesheet' id='walcf7-datepicker-css-css' href='https://www.nupco.com/wp-content/plugins/date-time-picker-for-contact-form-7/assets/css/jquery.datetimepicker.min.css?ver=1.0.0' type='text/css' media='all' />
<link rel='stylesheet' id='wpml-legacy-horizontal-list-0-css' href='//www.nupco.com/wp-content/plugins/sitepress-multilingual-cms/templates/language-switchers/legacy-list-horizontal/style.css?ver=1' type='text/css' media='all' />
<link rel='stylesheet' id='wpml-menu-item-0-css' href='//www.nupco.com/wp-content/plugins/sitepress-multilingual-cms/templates/language-switchers/menu-item/style.css?ver=1' type='text/css' media='all' />
<link rel='stylesheet' id='parent-style-css' href='https://www.nupco.com/wp-content/themes/zakra/style.css?ver=6.5.3' type='text/css' media='all' />
<link rel='stylesheet' id='child-style-css' href='https://www.nupco.com/wp-content/themes/Zakrachild/style.css?ver=1.0' type='text/css' media='all' />
<link rel='stylesheet' id='font-awesome-css' href='https://www.nupco.com/wp-content/plugins/elementor/assets/lib/font-awesome/css/font-awesome.min.css?ver=4.7.0' type='text/css' media='all' />
<link rel='stylesheet' id='zakra-style-rtl-css' href='https://www.nupco.com/wp-content/themes/Zakrachild/style-rtl.css?ver=6.5.3' type='text/css' media='all' />
<style id='zakra-style-inline-css' type='text/css'>
.tg-site-header .tg-site-header-top{color: #1c2346;}.tg-site-header .tg-site-header-top{background-color: #1c2346;background-image: ;background-repeat: repeat;background-position: center center;background-size: contain;background-attachment: scroll;}
@media (min-width: 1200px) {.tg-container{max-width: 1200px;}}
a:hover, a:focus,  .tg-primary-menu > div ul li:hover > a,  .tg-primary-menu > div ul li.current_page_item > a, .tg-primary-menu > div ul li.current-menu-item > a,  .tg-mobile-navigation > div ul li.current_page_item > a, .tg-mobile-navigation > div ul li.current-menu-item > a,  .entry-content a,  .tg-meta-style-two .entry-meta span, .tg-meta-style-two .entry-meta a{color: #1c2346;}.tg-primary-menu.tg-primary-menu--style-underline > div > ul > li.current_page_item > a::before, .tg-primary-menu.tg-primary-menu--style-underline > div > ul > li.current-menu-item > a::before, .tg-primary-menu.tg-primary-menu--style-left-border > div > ul > li.current_page_item > a::before, .tg-primary-menu.tg-primary-menu--style-left-border > div > ul > li.current-menu-item > a::before, .tg-primary-menu.tg-primary-menu--style-right-border > div > ul > li.current_page_item > a::before, .tg-primary-menu.tg-primary-menu--style-right-border > div > ul > li.current-menu-item > a::before, .tg-scroll-to-top:hover, button, input[type="button"], input[type="reset"], input[type="submit"], .tg-primary-menu > div ul li.tg-header-button-wrap a{background-color: #1c2346;}body{color: #1c2346;}
.tg-site-footer .tg-site-footer-bar{color: #e06e0e;}.tg-site-footer .tg-site-footer-bar{border-top-width: 1px;}.tg-site-footer .tg-site-footer-bar{border-top-color: #76797a;}.tg-site-footer .tg-site-footer-bar{background-color: #1c2346;background-image: ;background-repeat: repeat;background-position: center center;background-size: contain;background-attachment: scroll;}
.tg-site-footer-widgets{background-color: #1c2346;background-image: ;background-repeat: repeat;background-position: center center;background-size: contain;background-attachment: scroll;}.tg-site-footer .tg-site-footer-widgets{border-top-width: 0px;}.tg-site-footer .tg-site-footer-widgets .widget-title{color: #76797a;}.tg-site-footer .tg-site-footer-widgets, .tg-site-footer .tg-site-footer-widgets p{color: #878787;}.tg-site-footer .tg-site-footer-widgets a{color: #76797a;}.tg-site-footer .tg-site-footer-widgets ul li{border-bottom-width: 0px;}
.tg-scroll-to-top{color: #1c2346;}.tg-scroll-to-top:hover{color: #1c2346;}
.tg-primary-menu > div ul li a{font-family: -apple-system, blinkmacsystemfont, segoe ui, roboto, oxygen-sans, ubuntu, cantarell, helvetica neue, helvetica, arial, sans-serif;font-size: 1rem;line-height: 1.8;font-weight: 400;font-style: normal;}
</style>
<link rel='stylesheet' id='elementor-icons-css' href='https://www.nupco.com/wp-content/plugins/elementor/assets/lib/eicons/css/elementor-icons.min.css?ver=5.6.2' type='text/css' media='all' />
<link rel='stylesheet' id='elementor-animations-css' href='https://www.nupco.com/wp-content/plugins/elementor/assets/lib/animations/animations.min.css?ver=2.9.2' type='text/css' media='all' />
<link rel='stylesheet' id='elementor-frontend-css' href='https://www.nupco.com/wp-content/plugins/elementor/assets/css/frontend-rtl.min.css?ver=2.9.2' type='text/css' media='all' />
<link rel='stylesheet' id='elementor-global-css' href='https://www.nupco.com/wp-content/uploads/elementor/css/global.css?ver=1702207209' type='text/css' media='all' />
<link rel='stylesheet' id='cf7cf-style-css' href='https://www.nupco.com/wp-content/plugins/cf7-conditional-fields/style.css?ver=2.4.4' type='text/css' media='all' />
<link rel='stylesheet' id='google-fonts-1-css' href='https://fonts.googleapis.com/css?family=Roboto%3A100%2C100italic%2C200%2C200italic%2C300%2C300italic%2C400%2C400italic%2C500%2C500italic%2C600%2C600italic%2C700%2C700italic%2C800%2C800italic%2C900%2C900italic%7CRoboto+Slab%3A100%2C100italic%2C200%2C200italic%2C300%2C300italic%2C400%2C400italic%2C500%2C500italic%2C600%2C600italic%2C700%2C700italic%2C800%2C800italic%2C900%2C900italic&#038;ver=6.5.3' type='text/css' media='all' />
<script type="text/javascript" src="https://www.nupco.com/wp-includes/js/jquery/jquery.min.js?ver=3.7.1" id="jquery-core-js"></script>
<script type="text/javascript">
//<![CDATA[
window["_csrf_"] = "08d64261128410065885eb74f1141a934fb02a645c04ae3e9c0b5c720f665b0d4217ee78b2c56c376177641b7e0681b2018ae627d27046304c9eebc3e1f0602c1651586be9389e3fee1c50c1add86d40a6cd4b93993f3b1ab4ddab241b48d82e599a32cbb3d12f411577da7b217cbf39ed9d15eaca1b8022ee77a17fe2d5916a29b89c0df851f8a6a5e300f95675cb6d12e3f0498b8c11d79c3d1d9deb7980e4870405924acd8b682fe4494f7c74484026aa45ea5536180f0b0dbcda59a8ed89a868645cd856cb77bedc755669b93c83385f42de18aa0aff0875e3941b7cbb5e22acd535d57f341c64857a5092d763682f0115ebf01ad1d76afe10548fac75effa76c8f6685159b80f4b7a63bf7d288e81cdee78695a3e38b4731fdd7837564bc02529ae634eaed285f3bf2a6f5ee5f1dd9d3e695f5f114a79af07d29e13d9d6365a382c8a1ac8fd782bdecf5fa1e25526da21590c8ce2599a9b21cfea64095a9bd97b148f42cd7ed597d63783abdbf0b4a6a09dec9b17374a79e4e7ae524e904d51433b4720913787de24887455b2b3d5eb1fcdb5ae69c3226ac335b286c007e89ccbeb8385aeaa469f9781f949d0f040bd83b0dd3cf15445163a45e02a95f991c1297eca32744b66e2fa9744be79b5447e6510d3d8e2fa53cfdfe4505f13332ee70166cb4ad0ff6bfe8c29adfe4431cb2aafa75195583e44602d90bf7d3ee16c0a1d000d1b7682319a17952631073fbf86b376905cb9281da41fa0122d5f190ff118954da349f67c7021cacb629748456275e153497bc37e3c6c3d4856e16ada118205bcfb1cf6de3db416ac45c9bd0363da6c05a254858a1e95ba088b36b75aec5668291d1716dd077cf713b595e2e40d6e83996a140d5ee7602689e7935cbc9c7d0f8ed199287974f0e95cce21d4b118809ca1bb57c0e2426c7c6991b8e914ee85b2490a7b9c7f2dd30a6ece1fdd0967e071bfb4ae8042caf4aae48acd64ffd2f335aa486e6a92d954e65eae5b09834b2a71927b558634ee3d03cefe02dec0d0591463f3cd7b34b13e5a80975610e9ef92c3a54ad1095c17301e529ed99125365e0997c65fd8a70d958ee5ca5ff9d19700cf428f7a471629cbd61f08df7179fac866a4228fc482c4375b7a0e068909ae22f09aebd2221e432711249c2ab825c71c66b804a958070a4616ffc42115e4d386ad33613e6208ec8204682255e3a53e44d1dacde5d43f071126d82f5bdbd63a0571eaf8ff2db0c11e5db8cb3f2057b0fbfb9b62cd897ef77800d87c58bc0a48fb3f7db937a8e67449c5f895b3950672fa10000c00f981d87e71fb78a875c4221937d3095fb4a86de7a954ff083965b4942534d345a4a035d1e11db955116d1231e73b6b058d55aff733cd2c43c12ce3582975c02ffc5edea659dc2853f95e30fae74184589fec6966c4f8aa8646ab9cb3c9ed619862ea9ed7afd92d61403f43a0e2f7b0c6892456dcf5c4f36cc99b8a8e72e22daeebf0c356e47b726b9c2d2aac848fa2e79e7a6f772f73895d1f954f2cc929fff644ad441a4f16c64fab76f4541322620946e98f103ebad3e29d85d34ae0be20bc345790cef63b5fb38a1b6e850447b9419ca9a1cfd424c21e844a88c988927353be98429b68a3326eebf92cafd590f27d1235f705dc3d7f073cf88553e810a4ff6a48964adebdd6a88bbfa2782ba826420e36d1fed3ff5cd1ecc95d28868f2a36d897facbbbf274f6f9e68f9faef0dc7fcec8a21d16b46acb42e60c99a396dbef2b2e15949358c803049b5b3d746c7e03ed301e07a1ec20fb5b379076c0a6dcdc14fcf3d4e75e9bf65f51fc940d9a6ae886fce6bc9732108a34fb117fcb6ca54faa2fdd631bd9a61a9b826fec4e40599a09b5fe6268902d671c5444886977a50d55acfce5bb3163e8e335aa4481eb4a7e08de91a70ceaa56af1559ca39a96214596450b56030bce8ede085036ba122e1c48ecf2dea822e4644ec6690c2bbf97d86ce1648bc5da9f6617e044b1f2d84030c5fd41bdbb3f5ebf1f82bfd426692eb381041932f5320d87ae967920c0189020dd3199e43a985d416acb1204987590e4cfad36fbecf00227015752656c3e2c50b8dac081eb15ce245e7ffd84476d78d9b5b0c07b25b13292d76dc586a162c6be602f56c2618d1137a11d3ed46aef9ac39981c626e76c08b618e895a60742915f9b";
//]]>
</script><script type="text/javascript" src="/TSbd/0825d2cf13ab2000faae44d9da686ef85db8c4d82b4d0518fbc56c2433a9a924402d0be301fb891d?type=2"></script><script type="text/javascript" src="https://www.nupco.com/wp-includes/js/jquery/jquery-migrate.min.js?ver=3.4.1" id="jquery-migrate-js"></script>
<link rel="https://api.w.org/" href="https://www.nupco.com/wp-json/" /><link rel="alternate" type="application/json" href="https://www.nupco.com/wp-json/wp/v2/pages/3715" /><link rel="EditURI" type="application/rsd+xml" title="RSD" href="https://www.nupco.com/xmlrpc.php?rsd" />
<meta name="generator" content="WordPress 6.5.3" />
<link rel="canonical" href="https://www.nupco.com/%d8%a7%d9%84%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a7%d8%aa/" />
<link rel='shortlink' href='https://www.nupco.com/?p=3715' />
<link rel="alternate" type="application/json+oembed" href="https://www.nupco.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fwww.nupco.com%2F%25d8%25a7%25d9%2584%25d9%2585%25d9%2586%25d8%25a7%25d9%2581%25d8%25b3%25d8%25a7%25d8%25aa%2F" />
<link rel="alternate" type="text/xml+oembed" href="https://www.nupco.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fwww.nupco.com%2F%25d8%25a7%25d9%2584%25d9%2585%25d9%2586%25d8%25a7%25d9%2581%25d8%25b3%25d8%25a7%25d8%25aa%2F&#038;format=xml" />
<meta name="generator" content="WPML ver:4.3.6 stt:5,1;" />
<style type='text/css'> .ae_data .elementor-editor-element-setting {
            display:none !important;
            }
            </style>
<!-- Dynamic Widgets by QURL loaded - http://www.dynamic-widgets.com //-->
		<style type="text/css">
						.site-title,
			.site-description {
				position: absolute;
				clip: rect(1px, 1px, 1px, 1px);
			}

					</style>
		<style type="text/css" id="custom-background-css">
body.custom-background { background-color: #e0e0e0; }
</style>
	<link rel="icon" href="https://www.nupco.com/wp-content/uploads/2023/02/cropped-icon-nupco-6060-32x32.png" sizes="32x32" />
<link rel="icon" href="https://www.nupco.com/wp-content/uploads/2023/02/cropped-icon-nupco-6060-192x192.png" sizes="192x192" />
<link rel="apple-touch-icon" href="https://www.nupco.com/wp-content/uploads/2023/02/cropped-icon-nupco-6060-180x180.png" />
<meta name="msapplication-TileImage" content="https://www.nupco.com/wp-content/uploads/2023/02/cropped-icon-nupco-6060-270x270.png" />
		<style type="text/css" id="wp-custom-css">
			div#elementor-panel-state-loading{
	display: none !importanr;
}		</style>
		
	</head>

<body class="rtl page-template page-template-tenderpage page-template-tenderpage-php page page-id-3715 custom-background wp-custom-logo tg-site-layout--default tg-container--wide has-page-header has-breadcrumbs elementor-default elementor-kit-23650 elementor-page elementor-page-3715">
<!-- Google Tag Manager (noscript) --><noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-5MVWVFQ"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript><!-- End Google Tag Manager (noscript) -->

<div id="page" class="site tg-site">
				<a class="skip-link screen-reader-text" href="#content">تخطى إلى المحتوى</a>
		

	<header id="masthead" class="site-header tg-site-header tg-site-header--left">

		
		<div class="tg-site-header-top">
			<div class="tg-header-container tg-container tg-container--flex tg-container--flex-center">
				<div class="tg-header-top-left-content">

					<section id="text-8" class="widget widget_text">			<div class="textwidget"><p><i class="fa fa-phone"></i> ٩٦٦٩٢٠٠١٨١٨٤+      <i class="fa fa-envelope-o"></i> info@nupco.com  <i class="fa fa-map-marker"></i> شارع سعيد السلمي المدينة الرقمية الرياض، المملكة العربية السعودية</p>
</div>
		</section>
				</div>
				<!-- /.tg-header-top-left-content -->
				<div class="tg-header-top-right-content">

					<section id="custom_html-5" class="widget_text widget widget_custom_html"><div class="textwidget custom-html-widget"><div class="header-bar-social-icons"><a href="https://twitter.com/nupco"><i class="fa fa-twitter"></i></a>
<a href="https://www.linkedin.com/company/nupco-national-unified-procurement-medical-supplies-company-/"><i class="fa fa-linkedin"></i></a></div></div></section>
				</div>
				<!-- /.tg-header-top-right-content -->
			</div>
			<!-- /.tg-container -->
		</div>
		<!-- /.tg-site-header-top -->

		

	<div class="tg-site-header-bottom">
	<div class="tg-header-container tg-container tg-container--flex tg-container--flex-center tg-container--flex-space-between">

		
		<div class="site-branding">


			
<a href="https://www.nupco.com/" class="custom-logo-link" rel="home"><img width="2940" height="2223" src="https://www.nupco.com/wp-content/uploads/2023/02/Logo.png" class="custom-logo" alt="nupco" decoding="async" fetchpriority="high" srcset="https://www.nupco.com/wp-content/uploads/2023/02/Logo.png 2940w, https://www.nupco.com/wp-content/uploads/2023/02/Logo-300x227.png 300w, https://www.nupco.com/wp-content/uploads/2023/02/Logo-1024x774.png 1024w, https://www.nupco.com/wp-content/uploads/2023/02/Logo-768x581.png 768w, https://www.nupco.com/wp-content/uploads/2023/02/Logo-1536x1161.png 1536w, https://www.nupco.com/wp-content/uploads/2023/02/Logo-2048x1549.png 2048w, https://www.nupco.com/wp-content/uploads/2023/02/Logo-24x18.png 24w, https://www.nupco.com/wp-content/uploads/2023/02/Logo-36x27.png 36w, https://www.nupco.com/wp-content/uploads/2023/02/Logo-48x36.png 48w" sizes="(max-width: 2940px) 100vw, 2940px" /></a>
						<div class="site-info-wrap">
									<p class="site-title">
						<a href="https://www.nupco.com/" rel="home">nupco</a>
					</p>
								</div>

		</div><!-- .site-branding -->
				<nav id="site-navigation" class="main-navigation tg-primary-menu tg-primary-menu--style-underline">
				<div class="menu"><ul id="primary-menu" class="menu-primary"><li id="menu-item-15079" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-home menu-item-15079"><a href="https://www.nupco.com/">الرئيسية</a></li>
<li id="menu-item-3700" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-3700"><a href="#">لمحة عن نوبكو</a>
<ul class="sub-menu">
	<li id="menu-item-22358" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-22358"><a href="https://www.nupco.com/%d8%a7%d9%84%d8%a7%d8%b3%d8%aa%d8%af%d8%a7%d9%85%d8%a9/">الاستدامة</a></li>
	<li id="menu-item-3766" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-3766"><a href="https://www.nupco.com/%d9%84%d9%85%d8%ad%d8%a9-%d8%b9%d8%a7%d9%85%d8%a9/">لمحة عامة</a></li>
	<li id="menu-item-8143" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-8143"><a href="https://www.nupco.com/members/">مجلس الادارة</a></li>
	<li id="menu-item-12574" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-12574"><a href="https://www.nupco.com/category/%d8%a7%d9%84%d8%a3%d8%ae%d8%a8%d8%a7%d8%b1/">الأخبار</a></li>
	<li id="menu-item-9499" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-9499"><a href="https://www.nupco.com/externalnewsletter/">نشرة نوبكو</a></li>
	<li id="menu-item-3767" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-3767"><a target="_blank" rel="noopener" href="https://www.nupco.com/wp-content/uploads/2020/03/FAQ-v2.pdf">الأسئلة الشائعة</a></li>
	<li id="menu-item-7622" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-7622"><a href="https://www.nupco.com/wp-content/uploads/2021/09/الدليل-الإرشادي-الموحد-لرحلة-الموردين.pdf">الدليل الإرشادي الموحد لرحلة المورد</a></li>
</ul>
</li>
<li id="menu-item-4028" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-4028"><a href="#">الخدمات الإلكترونية</a>
<ul class="sub-menu">
	<li id="menu-item-17945" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-17945"><a href="https://inupco.nupco.com/suppliers/pre-registration">تسجيل الموردين</a></li>
	<li id="menu-item-4030" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4030"><a target="_blank" rel="noopener" href="https://tenders.nupco.com/irj/portal">مزود الخدمة الذاتية</a></li>
	<li id="menu-item-4031" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4031"><a target="_blank" rel="noopener" href="https://tenders.nupco.com/irj/portal">طلبات العملاء</a></li>
</ul>
</li>
<li id="menu-item-14427" class="menu-item menu-item-type-custom menu-item-object-custom current-menu-ancestor current-menu-parent menu-item-has-children menu-item-14427"><a href="#">المنافسات</a>
<ul class="sub-menu">
	<li id="menu-item-3768" class="menu-item menu-item-type-post_type menu-item-object-page current-menu-item page_item page-item-3715 current_page_item menu-item-3768"><a href="https://www.nupco.com/%d8%a7%d9%84%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a7%d8%aa/" aria-current="page">المنافسات المطروحة</a></li>
	<li id="menu-item-14633" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-14633"><a href="https://www.nupco.com/%d8%a7%d9%84%d8%a3%d8%b3%d8%a6%d9%84%d8%a9-%d8%a7%d9%84%d8%b4%d8%a7%d8%a6%d8%b9%d8%a9-%d8%a7%d9%84%d8%ae%d8%a7%d8%b5%d8%a9-%d8%a8%d8%a7%d9%84%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a7%d8%aa/">الأسئلة الشائعه الخاصة بالمنافسات</a></li>
</ul>
</li>
<li id="menu-item-22433" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-22433"><a href="https://www.nupco.com/%d8%a7%d9%84%d8%af%d9%84%d9%8a%d9%84-%d8%a7%d9%84%d9%85%d9%88%d8%ad%d8%af/">الدليل الموحد</a></li>
<li id="menu-item-25392" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-25392"><a href="#">التوظيف و التدريب</a>
<ul class="sub-menu">
	<li id="menu-item-4149" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4149"><a href="https://www.nupco.com/NupcoJobPortal/ar">التوظيف</a></li>
	<li id="menu-item-25391" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-25391"><a href="https://www.nupco.com/%d8%a7%d9%84%d8%aa%d8%af%d8%b1%d9%8a%d8%a8/">التدريب</a></li>
</ul>
</li>
<li id="menu-item-17595" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-17595"><a href="https://inupco.nupco.com/home"><img src="https://www.nupco.com/wp-content/uploads/2023/07/box.png"></a></li>
<li class="menu-item tg-menu-item tg-menu-item-search"><a><i class="tg-icon tg-icon-search"></i></a><form role="search" method="get" class="search-form" action="https://www.nupco.com/">
				<label>
					<span class="screen-reader-text">البحث عن:</span>
					<input type="search" class="search-field" placeholder="بحث &hellip;" value="" name="s" />
				</label>
				<input type="submit" class="search-submit" value="بحث" />
			</form></li><!-- /.tg-header-search --></ul></div>		</nav><!-- #site-navigation -->
				<nav id="header-action" class="tg-header-action">
			<ul class="tg-header-action-list">

				<li class="tg-header-action__item tg-mobile-toggle" >
										<i class="tg-icon tg-icon-bars"></i>
				</li>
				<!-- /.tg-mobile-toggle -->
			</ul>
			<!-- /.zakra-header-action-list -->
		</nav><!-- #header-action -->
				
	</div>
	<!-- /.tg-container -->
	</div>
	<!-- /.tg-site-header-bottom -->
		
	</header><!-- #masthead -->
		
	<main id="main" class="site-main">
		
		<header class="tg-page-header tg-page-header--left">
			<div class="tg-container tg-container--flex tg-container--flex-center tg-container--flex-space-between">
				<h1 class="tg-page-header__title">المنافسات</h1>
				<nav role="navigation" aria-label="العناوين (Breadcrumbs)" class="breadcrumb-trail breadcrumbs" itemprop="breadcrumb"><ul class="trail-items" itemscope itemtype="http://schema.org/BreadcrumbList"><meta name="numberOfItems" content="2" /><meta name="itemListOrder" content="Ascending" /><li itemprop="itemListElement" itemscope itemtype="http://schema.org/ListItem" class="trail-item"><a href="https://www.nupco.com/" rel="home" itemprop="item"><span itemprop="name">الصفحة الرئيسية</span></a><meta itemprop="position" content="1" /></li><li class="trail-item trail-end"><span>المنافسات</span></li></ul></nav>			</div>
		</header>
		<!-- /.page-header -->
				<div id="content" class="site-content">
			<div class="tg-container tg-container--flex tg-container--flex-space-between">
		

        <div class="tg-container tg-container_Tenders tg-container_Tenders_arbic" style="    max-width: 1200px;">
            <div class="row clearfix">
            	<div class="col-md-12 col-sm-12 col-xs-12 filter-box" style="width:100%; margin-top:40px;">
                <h4 style="text-align: center;font-family: CoHeadlineW23-ArabicRegular; margin-bottom: 40px;font-weight: 600;font-size: 30px;
">
تحقق من أحدث فرص المنافسات أدناه
</h4>
            </div>
                <div class="col-md-12 col-sm-12 col-xs-12 filter-box" style="width:100%">
                    <ul class="filter-tabs clearfix" style="margin-bottom:30px; float:right; width: 100%">
                        
                    
                 <li class="filter" data-role="button" data-filter="all"> عرض الكل </li>    
                         
                        
                    <li class="filter direct-purchase" data-role="button" data-filter=".direct-purchase1"> الشراء المباشر </li> 
                        
                        
                    <li class="filter first-results" data-role="button" data-filter=".first-results1"> النتائج الأولية </li> 
                        
                        
                    <li class="filter the-final-results" data-role="button" data-filter=".the-final-results1"> النتائج النهائية </li> 
                        
                        
                    <li class="filter under-sudying" data-role="button" data-filter=".under-sudying1"> تحت الدراسة </li> 
                        
                        
                    <li class="filter new" data-role="button" data-filter=".new1"> جديد </li> 
                        
                        
                    <li class="filter available" data-role="button" data-filter=".available1"> متاحة/جديد </li> 
                        
                        
                    <li class="filter canceled" data-role="button" data-filter=".canceled1"> ملغية </li> 
                                                <li style="background: #1c2346; float: left; margin-left:0px;"><a href="https://www.nupco.com/%d8%ae%d8%b7%d8%a9-%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a7%d8%aa-%d8%a7%d9%84%d8%b4%d8%b1%d8%a7%d8%a1-%d8%a7%d9%84%d9%85%d9%88%d8%ad%d8%af-%d8%a7%d9%84%d9%85%d8%ad%d8%af%d8%ab%d8%a9-%d9%84%d8%b9%d8%a7/" style="color:#fff;"> خطة المنافسات </a></li>
                    </ul>
                </div>
            </div>
            
            <div id="Container" class="row">                                 

                    

 
                    <style type="text/css">
                    	.filter-tabs li.active.new{background: #3b8dc7;}
                    </style>
                    <div class="column-box mix Tender_width  new1" data-myorder="35" style="background: rgba(59, 141, 199,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d8%a3%d9%87%d9%8a%d9%84-%d8%a7%d9%84%d8%b4%d8%b1%d9%83%d8%a7%d8%aa-%d8%a7%d9%84%d8%b5%d8%a7%d9%86%d8%b9%d8%a9-%d9%84%d8%aa%d9%88%d9%82%d9%8a%d8%b9-%d8%a7%d8%aa%d9%81%d8%a7%d9%82%d9%8a%d8%a9/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0048/24</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">جديد </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>تأهيل الشركات الصانعة لتوقيع اتفاقية خدمات مقابل الشراء (VALUE BASE AGREEMENT)</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الخميس 18-07-2024</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الخميس 18-07-2024</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.canceled{background: #76797a;}
                    </style>
                    <div class="column-box mix Tender_width  canceled1" data-myorder="38" style="background: rgba(118, 121, 122,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%88%d8%aa%d9%88%d8%b1%d9%8a%d8%af-%d8%a3%d8%ac%d9%87%d8%b2%d8%a9-%d9%85%d8%b9-%d9%85%d8%ad%d8%a7%d9%84%d9%8a%d9%84-%d9%88%d9%85-6/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0001/23</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">ملغية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين وتوريد أجهزة مع محاليل ومستهلكات خاصة بالمختبرات العامة للجهات الصحية الحكومية بنظام القيمة الثابتة لكل نتيجة مؤكدة GPPRR (المرحلة الثانية)</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الثلاثاء 06-06-2023</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الأربعاء 07-06-2023</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.canceled{background: #76797a;}
                    </style>
                    <div class="column-box mix Tender_width  canceled1" data-myorder="38" style="background: rgba(118, 121, 122,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%88%d8%aa%d9%88%d8%b1%d9%8a%d8%af-%d8%a3%d8%ac%d9%87%d8%b2%d8%a9-%d9%85%d8%b9-%d9%85%d8%ad%d8%a7%d9%84%d9%8a%d9%84-%d9%88%d9%85-8/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0039/23</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">ملغية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين وتوريد أجهزة مع محاليل ومستهلكات خاصة بالمختبرات العامة للجهات الصحية الحكومية بنظام القيمة الثابتة لكل نتيجة مؤكدة GPPRR  (المرحلة الثالثة)</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الإثنين 10-07-2023</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الثلاثاء 11-07-2023</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.canceled{background: #76797a;}
                    </style>
                    <div class="column-box mix Tender_width  canceled1" data-myorder="38" style="background: rgba(118, 121, 122,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d9%82%d8%af%d9%8a%d9%85-%d8%ae%d8%af%d9%85%d8%a9-%d8%a7%d9%84%d8%ba%d8%b3%d9%8a%d9%84-%d8%a7%d9%84%d9%83%d9%84%d9%88%d9%8a-%d9%81%d9%8a-%d8%a7%d9%84%d9%85%d9%86%d8%a7%d8%b2%d9%84-%d9%84%d9%84/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0042/23</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">ملغية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>تقديم خدمة الغسيل الكلوي في المنازل للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأربعاء 04-10-2023</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الخميس 05-10-2023</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.first-results{background: #963149;}
                    </style>
                    <div class="column-box mix Tender_width  first-results1" data-myorder="34" style="background: rgba(150, 49, 73,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d8%a3%d8%af%d9%88%d9%8a%d8%a9-%d8%b9%d9%84%d8%a7%d8%ac-%d8%a3%d9%85%d8%b1%d8%a7%d8%b6-%d8%a7%d9%84%d8%b3%d9%84-%d9%88%d8%a7%d9%84/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0044/23</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج الأولية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين أدوية علاج أمراض السل والملاريا والليشمانيا</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأحد 14-01-2024</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الإثنين 15-01-2024</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.first-results{background: #963149;}
                    </style>
                    <div class="column-box mix Tender_width  first-results1" data-myorder="34" style="background: rgba(150, 49, 73,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%a7%d9%84%d9%85%d8%b9%d9%82%d9%85%d8%a7%d8%aa/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0048/23</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج الأولية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين مستلزمات المعقمات</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الثلاثاء 16-01-2024</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الأربعاء 17-01-2024</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.first-results{background: #963149;}
                    </style>
                    <div class="column-box mix Tender_width  first-results1" data-myorder="34" style="background: rgba(150, 49, 73,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%a7%d9%84%d8%b9%d9%8a%d9%88%d9%86/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0047/23</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج الأولية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين مستلزمات العيون</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الإثنين 29-01-2024</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الثلاثاء 30-01-2024</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.first-results{background: #963149;}
                    </style>
                    <div class="column-box mix Tender_width  first-results1" data-myorder="34" style="background: rgba(150, 49, 73,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%a7%d9%84%d8%a3%d8%b4%d8%b9%d8%a9-%d8%a7%d9%84%d8%aa%d8%af%d8%a7%d8%ae%d9%84-3/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0004/24</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج الأولية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين مستلزمات الأشعة التداخلية وقسطرة القلب</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأحد 11-02-2024</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الإثنين 12-02-2024</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.first-results{background: #963149;}
                    </style>
                    <div class="column-box mix Tender_width  first-results1" data-myorder="34" style="background: rgba(150, 49, 73,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d9%84%d9%84%d8%ac%d9%87%d8%a7%d8%aa-%d8%a7%d9%84%d8%b5%d8%ad%d9%8a%d8%a9-%d8%a7%d9%84%d8%ad%d9%83%d9%88%d9%85%d9%8a-2/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NDP0235/24</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج الأولية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>تأمين مستلزمات للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأربعاء 20-03-2024</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الأربعاء 20-03-2024</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.available{background: #3b8dc7;}
                    </style>
                    <div class="column-box mix Tender_width  available1" data-myorder="36" style="background: rgba(59, 141, 199,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%b7%d9%84%d8%a8-%d9%85%d8%b9%d9%84%d9%88%d9%85%d8%a7%d8%aa-%d8%a7%d9%84%d8%a7%d8%b3%d8%aa%d8%b9%d8%a7%d9%86%d8%a9-%d8%a8%d9%85%d8%b5%d8%a7%d8%af%d8%b1-%d8%ae%d8%a7%d8%b1%d8%ac%d9%8a%d8%a9-%d9%84/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0049/24</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">متاحة/جديد </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>طلب معلومات الاستعانة بمصادر خارجية لخدمات الأشعة الطبية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الخميس 18-04-2024</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الخميس 18-04-2024</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.available{background: #3b8dc7;}
                    </style>
                    <div class="column-box mix Tender_width  available1" data-myorder="36" style="background: rgba(59, 141, 199,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/25036-2/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0019/24</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">متاحة/جديد </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين مستلزمات التأهيل والعلاج الطبيعي</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأربعاء 26-06-2024</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الخميس 27-06-2024</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.available{background: #3b8dc7;}
                    </style>
                    <div class="column-box mix Tender_width  available1" data-myorder="36" style="background: rgba(59, 141, 199,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a7%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d9%85%d9%86%d8%a7%d8%b8%d9%8a%d8%b1-%d8%a7%d9%84%d8%ac%d9%87%d8%a7%d8%b2-%d8%a7/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0015/24</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">متاحة/جديد </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تامين مستلزمات مناظير الجهاز الهضمي</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأحد 30-06-2024</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الإثنين 01-07-2024</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.available{background: #3b8dc7;}
                    </style>
                    <div class="column-box mix Tender_width  available1" data-myorder="36" style="background: rgba(59, 141, 199,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%a7%d9%84%d8%a3%d8%af%d9%88%d9%8a%d8%a9-%d8%a7%d9%84%d9%85%d8%ae%d8%af%d8%b1%d8%a9-%d9%88%d8%a7%d9%84%d9%85%d9%82%d9%8a%d8%af%d8%a9/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0032/24</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">متاحة/جديد </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة الأدوية المخدرة والمقيدة</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الإثنين 01-07-2024</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الثلاثاء 02-07-2024</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.available{background: #3b8dc7;}
                    </style>
                    <div class="column-box mix Tender_width  available1" data-myorder="36" style="background: rgba(59, 141, 199,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d9%88%d9%85%d8%ad%d8%a7%d9%84%d9%8a%d9%84-%d9%84%d8%a3%d9%82%d8%b3%d8%a7%d9%85/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0017/24</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">متاحة/جديد </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين مستلزمات ومحاليل لأقسام علم أمراض الأنسجة والكيمياء النسيجية المناعية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الثلاثاء 02-07-2024</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الأربعاء 03-07-2024</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.available{background: #3b8dc7;}
                    </style>
                    <div class="column-box mix Tender_width  available1" data-myorder="36" style="background: rgba(59, 141, 199,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%a7%d9%84%d8%a3%d8%b3%d9%86%d8%a7%d9%86-%d8%a7%d9%84%d8%b9%d8%a7%d9%85%d8%a9/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0031/24</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">متاحة/جديد </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين مستلزمات الأسنان العامة</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأحد 14-07-2024</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الإثنين 15-07-2024</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.available{background: #3b8dc7;}
                    </style>
                    <div class="column-box mix Tender_width  available1" data-myorder="36" style="background: rgba(59, 141, 199,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d9%82%d8%af%d9%8a%d9%85-%d8%ae%d8%af%d9%85%d8%a7%d8%aa-%d8%a7%d9%84%d8%ba%d8%b3%d9%8a%d9%84-%d8%a7%d9%84%d9%83%d9%84%d9%88%d9%8a/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0046/23</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">متاحة/جديد </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تقديم خدمات الغسيل الكلوي</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأحد 04-08-2024</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الإثنين 05-08-2024</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.available{background: #3b8dc7;}
                    </style>
                    <div class="column-box mix Tender_width  available1" data-myorder="36" style="background: rgba(59, 141, 199,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d8%a7%d9%84%d9%85%d8%ad%d8%a7%d9%84%d9%8a%d9%84-%d8%a7%d9%84%d9%88%d8%b1%d9%8a%d8%af%d9%8a%d8%a9-%d9%88%d8%a3%d8%af%d9%88%d9%8a-2/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0041/24</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">متاحة/جديد </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين المحاليل الوريدية وأدوية التغذية الوريدية المتكاملة</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأربعاء 24-07-2024</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الخميس 25-07-2024</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.under-sudying{background: #f1c52c;}
                    </style>
                    <div class="column-box mix Tender_width  under-sudying1" data-myorder="42" style="background: rgba(241, 197, 44,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%b7%d9%84%d8%a8-%d9%85%d8%b9%d9%84%d9%88%d9%85%d8%a7%d8%aa-%d8%aa%d8%ae%d8%b5-%d9%85%d8%b1%d8%a7%d9%83%d8%b2-%d8%a3%d9%85%d8%b1%d8%a7%d8%b6-%d8%a7%d9%84%d8%b3%d9%83%d8%b1%d9%8a-%d9%84%d9%84%d8%ac/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0045/23</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">تحت الدراسة </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>طلب معلومات تخص مراكز أمراض السكري للجهات الصحية الحكومية (DIABETIC CENTER SERVICES) بنظام القيمة مقابل الشراء (Value-Based)</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الخميس 12-10-2023</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الخميس 12-10-2023</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.under-sudying{background: #f1c52c;}
                    </style>
                    <div class="column-box mix Tender_width  under-sudying1" data-myorder="42" style="background: rgba(241, 197, 44,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%a7%d9%84%d8%b9%d8%b8%d8%a7%d9%85-%d9%88%d8%a7%d9%84%d8%b9%d9%85%d9%88%d8%af-2/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0035/23</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">تحت الدراسة </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين مستلزمات العظام والعمود الفقري</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الثلاثاء 27-02-2024</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الأربعاء 28-02-2024</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.under-sudying{background: #f1c52c;}
                    </style>
                    <div class="column-box mix Tender_width  under-sudying1" data-myorder="42" style="background: rgba(241, 197, 44,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d8%a7%d9%84%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%a7%d9%84%d8%b7%d8%a8%d9%8a%d8%a9-%d8%a7%d9%84%d8%b9%d8%a7%d9%85/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0001/24</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">تحت الدراسة </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين المستلزمات الطبية العامة (تمريض والعناية بالجروح)</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأحد 18-02-2024</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الإثنين 19-02-2024</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.under-sudying{background: #f1c52c;}
                    </style>
                    <div class="column-box mix Tender_width  under-sudying1" data-myorder="42" style="background: rgba(241, 197, 44,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%a7%d9%84%d8%b9%d9%84%d8%a7%d8%ac-%d8%a7%d9%84%d8%aa%d9%86%d9%81%d8%b3%d9%8a-2/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0002/24</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">تحت الدراسة </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين مستلزمات العلاج التنفسي والتخدير</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الإثنين 04-03-2024</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الثلاثاء 05-03-2024</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.under-sudying{background: #f1c52c;}
                    </style>
                    <div class="column-box mix Tender_width  under-sudying1" data-myorder="42" style="background: rgba(241, 197, 44,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%a7%d9%84%d8%ba%d8%b3%d9%8a%d9%84-%d8%a7%d9%84%d9%83%d9%84%d9%88%d9%8a-%d9%88/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0003/24</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">تحت الدراسة </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين مستلزمات الغسيل الكلوي والكلية الصناعية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأربعاء 06-03-2024</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الخميس 07-03-2024</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.under-sudying{background: #f1c52c;}
                    </style>
                    <div class="column-box mix Tender_width  under-sudying1" data-myorder="42" style="background: rgba(241, 197, 44,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%a7%d9%84%d8%b9%d9%82%d9%85-%d9%88%d8%a7%d9%84%d8%a5%d8%ae%d8%b5%d8%a7%d8%a8-2/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0005/24</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">تحت الدراسة </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين مستلزمات العقم والإخصاب</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الثلاثاء 19-03-2024</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الأربعاء 20-03-2024</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.under-sudying{background: #f1c52c;}
                    </style>
                    <div class="column-box mix Tender_width  under-sudying1" data-myorder="42" style="background: rgba(241, 197, 44,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%a7%d9%84%d8%a3%d8%b7%d8%b1%d8%a7%d9%81-%d8%a7%d9%84%d8%b5%d9%86%d8%a7%d8%b9-2/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0008/24</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">تحت الدراسة </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين مستلزمات الأطراف الصناعية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأحد 28-04-2024</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الإثنين 29-04-2024</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.under-sudying{background: #f1c52c;}
                    </style>
                    <div class="column-box mix Tender_width  under-sudying1" data-myorder="42" style="background: rgba(241, 197, 44,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%a7%d9%84%d8%ac%d8%b1%d8%a7%d8%ad%d8%a9/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0006/24</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">تحت الدراسة </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين مستلزمات الجراحة</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الإثنين 18-03-2024</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الثلاثاء 19-03-2024</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.under-sudying{background: #f1c52c;}
                    </style>
                    <div class="column-box mix Tender_width  under-sudying1" data-myorder="42" style="background: rgba(241, 197, 44,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%ac%d8%b1%d8%a7%d8%ad%d8%a9-%d8%a7%d9%84%d9%82%d9%84%d8%a8-%d9%88%d8%a7%d9%84-3/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0009/24</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">تحت الدراسة </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين مستلزمات جراحة القلب والأوعية الدموية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الإثنين 22-04-2024</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الثلاثاء 23-04-2024</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.under-sudying{background: #f1c52c;}
                    </style>
                    <div class="column-box mix Tender_width  under-sudying1" data-myorder="42" style="background: rgba(241, 197, 44,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%a7%d9%84%d8%aa%d8%b9%d9%82%d9%8a%d9%85-%d8%b1%d9%82%d9%85-npt0007-24/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0007/24</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">تحت الدراسة </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين مستلزمات التعقيم  رقم NPT0007/24</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأحد 21-04-2024</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الإثنين 22-04-2024</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.under-sudying{background: #f1c52c;}
                    </style>
                    <div class="column-box mix Tender_width  under-sudying1" data-myorder="42" style="background: rgba(241, 197, 44,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%a7%d9%84%d8%ae%d9%8a%d9%88%d8%b7-%d8%a7%d9%84%d8%ac%d8%b1%d8%a7%d8%ad%d9%8a/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0010/24</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">تحت الدراسة </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين مستلزمات الخيوط الجراحية وجراحة المناظير والجراح الآلي</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأربعاء 08-05-2024</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الخميس 09-05-2024</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.under-sudying{background: #f1c52c;}
                    </style>
                    <div class="column-box mix Tender_width  under-sudying1" data-myorder="42" style="background: rgba(241, 197, 44,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/24677-2/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0014/24</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">تحت الدراسة </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين الأدوية التكميلية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الثلاثاء 28-05-2024</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الأربعاء 29-05-2024</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.under-sudying{background: #f1c52c;}
                    </style>
                    <div class="column-box mix Tender_width  under-sudying1" data-myorder="42" style="background: rgba(241, 197, 44,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d9%82%d8%af%d9%8a%d9%85-%d9%86%d8%aa%d8%a7%d8%a6%d8%ac-%d9%81%d8%ad%d9%88%d8%b5%d8%a7%d8%aa-%d9%85%d8%ae%d8%a8%d8%b1%d9%8a%d8%a9-%d8%b9%d9%86-%d8%b7%d8%b1-3/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0012/24</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">تحت الدراسة </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تقديم نتائج فحوصات مخبرية عن طريق إرسالها لمختبرات مرجعية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأحد 26-05-2024</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الإثنين 27-05-2024</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.under-sudying{background: #f1c52c;}
                    </style>
                    <div class="column-box mix Tender_width  under-sudying1" data-myorder="42" style="background: rgba(241, 197, 44,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/25020-2/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0016/24</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">تحت الدراسة </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين مستلزمات ومحاليل المختبرات لقسم الأحياء الدقيقة والجزيئية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأحد 02-06-2024</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الإثنين 03-06-2024</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.under-sudying{background: #f1c52c;}
                    </style>
                    <div class="column-box mix Tender_width  under-sudying1" data-myorder="42" style="background: rgba(241, 197, 44,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%ac%d8%b1%d8%a7%d8%ad%d8%a9-%d8%a7%d9%84%d9%88%d8%ac%d9%87-%d9%88%d8%a7%d9%84/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0025/24</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">تحت الدراسة </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين مستلزمات جراحة الوجه والفكين وزراعة الاسنان</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأربعاء 22-05-2024</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الخميس 23-05-2024</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.under-sudying{background: #f1c52c;}
                    </style>
                    <div class="column-box mix Tender_width  under-sudying1" data-myorder="42" style="background: rgba(241, 197, 44,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d8%a7%d9%84%d8%aa%d8%ba%d8%b0%d9%8a%d8%a9-%d8%a7%d9%84%d8%b9%d9%84%d8%a7%d8%ac%d9%8a%d8%a9/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0020/24</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">تحت الدراسة </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين التغذية العلاجية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأربعاء 05-06-2024</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الخميس 06-06-2024</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.direct-purchase{background: ;}
                    </style>
                    <div class="column-box mix Tender_width  direct-purchase1" data-myorder="71" style="background: rgba(0, 0, 0,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d9%84%d9%84%d8%ac%d9%87%d8%a7%d8%aa-%d8%a7%d9%84%d8%b5%d8%ad%d9%8a%d8%a9-%d8%a7%d9%84%d8%ad%d9%83%d9%88%d9%85%d9%8a-14/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NDP0502/24</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">الشراء المباشر </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>تأمين مستلزمات للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأربعاء 12-06-2024</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الأربعاء 12-06-2024</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.direct-purchase{background: ;}
                    </style>
                    <div class="column-box mix Tender_width  direct-purchase1" data-myorder="71" style="background: rgba(0, 0, 0,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d9%84%d9%84%d8%ac%d9%87%d8%a7%d8%aa-%d8%a7%d9%84%d8%b5%d8%ad%d9%8a%d8%a9-%d8%a7%d9%84%d8%ad%d9%83%d9%88%d9%85%d9%8a-16/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NDP0501/24</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">الشراء المباشر </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>تأمين مستلزمات للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأربعاء 12-06-2024</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الأربعاء 12-06-2024</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.direct-purchase{background: ;}
                    </style>
                    <div class="column-box mix Tender_width  direct-purchase1" data-myorder="71" style="background: rgba(0, 0, 0,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d8%a5%d8%ad%d8%aa%d9%8a%d8%a7%d8%ac-%d9%85%d8%af%d9%8a%d9%86%d8%a9-%d8%a7%d9%84%d9%85%d9%84%d9%83-%d8%b9%d8%a8%d8%af%d8%a7%d9%84%d8%b9%d8%b2%d9%8a%d8%b2-%d8%a7%d9%84/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NDP0506/24</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">الشراء المباشر </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>تأمين إحتياج مدينة الملك عبدالعزيز الطبية &#8211; تمديد</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الثلاثاء 11-06-2024</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الثلاثاء 11-06-2024</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.direct-purchase{background: ;}
                    </style>
                    <div class="column-box mix Tender_width  direct-purchase1" data-myorder="71" style="background: rgba(0, 0, 0,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d8%aa%d8%ac%d9%87%d9%8a%d8%b2-%d8%a3%d9%82%d8%b3%d8%a7%d9%85-%d8%a7%d9%84%d9%85%d8%ae%d8%aa%d8%a8%d8%b1%d8%a7%d8%aa-%d9%88%d8%a8%d9%86%d9%83-%d8%a7%d9%84%d8%af%d9%85/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NDP0342/24</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">الشراء المباشر </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>تأمين تجهيز أقسام المختبرات وبنك الدم &#8211; تمـديـد</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الثلاثاء 11-06-2024</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الثلاثاء 11-06-2024</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.direct-purchase{background: ;}
                    </style>
                    <div class="column-box mix Tender_width  direct-purchase1" data-myorder="71" style="background: rgba(0, 0, 0,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d8%a7%d8%ad%d8%aa%d9%8a%d8%a7%d8%ac-%d9%85%d8%b3%d8%aa%d8%b4%d9%81%d9%89-%d8%a7%d9%84%d9%85%d9%84%d9%83-%d9%81%d9%8a%d8%b5%d9%84-%d8%a8%d8%ac%d8%af%d8%a9/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NDP0519/24</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">الشراء المباشر </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>تأمين احتياج مستشفى الملك فيصل بجدة &#8211; تمديد</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الخميس 13-06-2024</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الخميس 13-06-2024</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.direct-purchase{background: ;}
                    </style>
                    <div class="column-box mix Tender_width  direct-purchase1" data-myorder="71" style="background: rgba(0, 0, 0,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d8%a8%d9%86%d9%88%d8%af-%d9%85%d8%ae%d8%aa%d8%a8%d8%b1%d8%a7%d8%aa-%d8%b9%d8%a7%d8%ac%d9%84%d8%a9/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NDP522/24</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">الشراء المباشر </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>تأمين بنود مختبرات عاجلة</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأربعاء 12-06-2024</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الأربعاء 12-06-2024</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.direct-purchase{background: ;}
                    </style>
                    <div class="column-box mix Tender_width  direct-purchase1" data-myorder="71" style="background: rgba(0, 0, 0,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%b7%d8%a8%d9%8a%d8%a9-%d9%84%d8%b5%d8%a7%d9%84%d8%ad-%d8%a7%d9%84%d8%ac%d9%87%d8%a7%d8%aa-%d8%a7%d9%84%d8%b5%d8%ad%d9%8a%d8%a9-%d8%a7%d9%84%d8%ad-3/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NDP0521/24</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">الشراء المباشر </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>مستلزمات طبية لصالح الجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الإثنين 10-06-2024</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الإثنين 10-06-2024</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.direct-purchase{background: ;}
                    </style>
                    <div class="column-box mix Tender_width  direct-purchase1" data-myorder="71" style="background: rgba(0, 0, 0,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d8%a8%d9%86%d9%88%d8%af-%d8%a7%d8%af%d9%88%d9%8a%d8%a9-%d9%84%d9%85%d9%86%d8%b5%d8%a9-%d8%a7%d9%84%d8%b3%d9%88%d9%82-%d8%a7%d9%84%d8%a5%d9%84%d9%83%d8%aa%d8%b1%d9%88-2/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NDP0516/24</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">الشراء المباشر </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>تأمين بنود ادوية لمنصة السوق الإلكتروني</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الثلاثاء 11-06-2024</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الثلاثاء 11-06-2024</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.direct-purchase{background: ;}
                    </style>
                    <div class="column-box mix Tender_width  direct-purchase1" data-myorder="71" style="background: rgba(0, 0, 0,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d8%a7%d8%ad%d8%aa%d9%8a%d8%a7%d8%ac-%d9%85%d8%af%d9%8a%d9%86%d8%a9-%d8%a7%d9%84%d9%85%d9%84%d9%83-%d8%b9%d8%a8%d8%af%d8%a7%d9%84%d9%84%d9%87-%d8%a7%d9%84%d8%b7%d8%a8/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NDP0525/24</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">الشراء المباشر </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>تأمين احتياج مدينة الملك عبدالله الطبية بمكة</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الإثنين 10-06-2024</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الإثنين 10-06-2024</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.direct-purchase{background: ;}
                    </style>
                    <div class="column-box mix Tender_width  direct-purchase1" data-myorder="71" style="background: rgba(0, 0, 0,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%b7%d8%a8%d9%8a%d8%a9-%d9%84%d8%b5%d8%a7%d9%84%d8%ad-%d8%a7%d9%84%d8%ac%d9%87%d8%a7%d8%aa-%d8%a7%d9%84%d8%b5%d8%ad%d9%8a%d8%a9-%d8%a7%d9%84%d8%ad-4/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NDP0523/24</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">الشراء المباشر </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>مستلزمات طبية لصالح الجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الإثنين 10-06-2024</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الإثنين 10-06-2024</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.direct-purchase{background: ;}
                    </style>
                    <div class="column-box mix Tender_width  direct-purchase1" data-myorder="71" style="background: rgba(0, 0, 0,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%b7%d8%a8%d9%8a%d8%a9-%d9%84%d8%b5%d8%a7%d9%84%d8%ad-%d8%a7%d9%84%d8%ac%d9%87%d8%a7%d8%aa-%d8%a7%d9%84%d8%b5%d8%ad%d9%8a%d8%a9-%d8%a7%d9%84%d8%ad-5/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NDP0524/24</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">الشراء المباشر </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>مستلزمات طبية لصالح الجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأربعاء 12-06-2024</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الأربعاء 12-06-2024</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.direct-purchase{background: ;}
                    </style>
                    <div class="column-box mix Tender_width  direct-purchase1" data-myorder="71" style="background: rgba(0, 0, 0,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d8%a7%d8%ad%d8%aa%d9%8a%d8%a7%d8%ac-%d8%ac%d8%a7%d9%85%d8%b9%d8%a9-%d8%a7%d9%84%d8%a3%d9%85%d9%8a%d8%b1%d8%a9-%d9%86%d9%88%d8%b1%d8%a9/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p> NDP0529/24</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">الشراء المباشر </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>تأمين احتياج جامعة الأميرة نورة</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأربعاء 12-06-2024</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الأربعاء 12-06-2024</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.direct-purchase{background: ;}
                    </style>
                    <div class="column-box mix Tender_width  direct-purchase1" data-myorder="71" style="background: rgba(0, 0, 0,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d8%a7%d8%ad%d8%aa%d9%8a%d8%a7%d8%ac-%d9%85%d8%b3%d8%aa%d8%b4%d9%81%d9%89-%d8%a7%d9%84%d9%85%d9%84%d9%83-%d8%ae%d8%a7%d9%84%d8%af-%d8%a7%d9%84%d8%aa%d8%ae%d8%b5%d8%b5/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NDP0531/24</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">الشراء المباشر </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>تأمين احتياج مستشفى الملك خالد التخصصي</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الثلاثاء 11-06-2024</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الثلاثاء 11-06-2024</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.direct-purchase{background: ;}
                    </style>
                    <div class="column-box mix Tender_width  direct-purchase1" data-myorder="71" style="background: rgba(0, 0, 0,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d8%a8%d9%86%d9%88%d8%af-%d8%a3%d8%af%d9%88%d9%8a%d8%a9-%d9%84%d8%b5%d8%a7%d9%84%d8%ad-%d9%86%d9%88%d8%a8%d9%83%d9%88/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NDP0530/24</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">الشراء المباشر </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>تأمين بنود أدوية لصالح نوبكو</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأربعاء 12-06-2024</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الأربعاء 12-06-2024</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.direct-purchase{background: ;}
                    </style>
                    <div class="column-box mix Tender_width  direct-purchase1" data-myorder="71" style="background: rgba(0, 0, 0,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%b7%d8%a8%d9%8a%d8%a9-%d9%84%d8%b5%d8%a7%d9%84%d8%ad-%d8%a7%d9%84%d8%ac%d9%87%d8%a7%d8%aa-%d8%a7%d9%84%d8%b5%d8%ad%d9%8a%d8%a9-%d8%a7%d9%84%d8%ad-6/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NDP0527/24</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">الشراء المباشر </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>مستلزمات طبية لصالح الجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الثلاثاء 11-06-2024</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الثلاثاء 11-06-2024</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.direct-purchase{background: ;}
                    </style>
                    <div class="column-box mix Tender_width  direct-purchase1" data-myorder="71" style="background: rgba(0, 0, 0,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d8%a8%d9%86%d9%88%d8%af-%d8%a7%d8%af%d9%88%d9%8a%d8%a9-%d9%84%d9%85%d9%86%d8%b5%d8%a9-%d8%a7%d9%84%d8%b3%d9%88%d9%82-%d8%a7%d9%84%d8%a5%d9%84%d9%83%d8%aa%d8%b1%d9%88-3/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NDP0532/24</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">الشراء المباشر </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>تأمين بنود ادوية لمنصة السوق الإلكتروني</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الثلاثاء 11-06-2024</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الثلاثاء 11-06-2024</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.direct-purchase{background: ;}
                    </style>
                    <div class="column-box mix Tender_width  direct-purchase1" data-myorder="71" style="background: rgba(0, 0, 0,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%a8%d9%86%d9%88%d8%af-%d8%b7%d8%a8%d9%8a%d8%a9-%d9%84%d8%b5%d8%a7%d9%84%d8%ad-%d8%a7%d9%84%d8%ac%d9%87%d8%a7%d8%aa-%d8%a7%d9%84%d8%b5%d8%ad%d9%8a%d8%a9-%d8%a7%d9%84%d8%ad%d9%83%d9%88%d9%85%d9%8a/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NDP0534/24</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">الشراء المباشر </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>بنود طبية لصالح الجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأربعاء 12-06-2024</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الأربعاء 12-06-2024</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.direct-purchase{background: ;}
                    </style>
                    <div class="column-box mix Tender_width  direct-purchase1" data-myorder="71" style="background: rgba(0, 0, 0,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d9%88%d9%85%d8%ad%d8%a7%d9%84%d9%8a%d9%84-%d8%a7%d9%84%d9%85%d8%ae%d8%aa%d8%a8-3/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p> NDP0535/24</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">الشراء المباشر </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين مستلزمات ومحاليل المختبرات لصالح جامعة الأميرة نورة</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الخميس 13-06-2024</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الخميس 13-06-2024</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.direct-purchase{background: ;}
                    </style>
                    <div class="column-box mix Tender_width  direct-purchase1" data-myorder="71" style="background: rgba(0, 0, 0,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d8%aa%d9%88%d8%b1%d9%8a%d8%af-%d9%88%d8%aa%d8%b1%d9%83%d9%8a%d8%a8-%d8%a3%d8%ac%d9%87%d8%b2%d8%a9-%d8%b7%d8%a8%d9%8a%d8%a9-%d9%84%d8%aa%d8%b7%d9%88%d9%8a%d8%b1-%d9%85/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NDP0515/24</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">الشراء المباشر </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>تأمين توريد وتركيب أجهزة طبية لتطوير مركز مناظير وجراحات المسالك البولية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الثلاثاء 11-06-2024</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الثلاثاء 11-06-2024</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.direct-purchase{background: ;}
                    </style>
                    <div class="column-box mix Tender_width  direct-purchase1" data-myorder="71" style="background: rgba(0, 0, 0,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%b7%d8%a8%d9%8a%d8%a9-%d9%84%d9%84%d8%ac%d9%87%d8%a7%d8%aa-%d8%a7%d9%84%d8%b5%d8%ad%d9%8a%d8%a9-%d8%a7%d9%84%d8%ad-20/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NDP0537/24</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">الشراء المباشر </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>تأمين مستلزمات طبية للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الإثنين 17-06-2024</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الإثنين 17-06-2024</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d8%a7%d9%84%d8%a3%d8%af%d9%88%d9%8a%d8%a9-%d8%a7%d9%84%d9%85%d8%ae%d8%af%d8%b1%d8%a9-%d9%88%d8%a7%d9%84%d9%85%d9%82%d9%8a%d8%af%d8%a9-%d9%84%d8%b9%d8%a7%d9%85-2022/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0004/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>تأمين الأدوية المخدرة والمقيدة لعام 2022م</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأربعاء 06-04-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الخميس 07-04-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d9%88%d9%82%d9%8a%d8%b9-%d8%a7%d8%aa%d9%81%d8%a7%d9%82%d9%8a%d8%a7%d8%aa-%d8%a7%d8%b7%d8%a7%d8%b1%d9%8a%d8%a9-%d9%84%d8%aa%d9%88%d8%b1%d9%8a%d8%af-%d8%a3%d8%ac%d9%87%d8%b2%d8%a9-%d8%a7%d9%84/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0001/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>توقيع اتفاقيات اطارية لتوريد أجهزة الثلاجات والمجمدات للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأحد 24-04-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الإثنين 25-04-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d9%88%d9%82%d9%8a%d8%b9-%d8%a7%d8%aa%d9%81%d8%a7%d9%82%d9%8a%d8%a7%d8%aa-%d8%a7%d8%b7%d8%a7%d8%b1%d9%8a%d8%a9-%d9%84%d8%aa%d9%88%d8%b1%d9%8a%d8%af-%d8%a3%d8%ac%d9%87%d8%b2%d8%a9-%d8%a7%d9%84-2/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0002/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>توقيع اتفاقيات اطارية لتوريد أجهزة الغسيل الكلوي للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأربعاء 20-04-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الخميس 21-04-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d9%88%d9%82%d9%8a%d8%b9-%d8%a7%d8%aa%d9%81%d8%a7%d9%82%d9%8a%d8%a7%d8%aa-%d8%a7%d8%b7%d8%a7%d8%b1%d9%8a%d8%a9-%d8%aa%d9%88%d8%b1%d9%8a%d8%af-%d9%88-%d8%aa%d8%b1%d9%83%d9%8a%d8%a8-%d9%88%d8%aa/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0003/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>توقيع اتفاقيات اطارية توريد و تركيب وتجهيز أجهزة عيادات الأسنان للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الثلاثاء 24-05-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الأربعاء 25-05-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d9%88%d9%82%d9%8a%d8%b9-%d8%a7%d8%aa%d9%81%d8%a7%d9%82%d9%8a%d8%a7%d8%aa-%d8%a7%d8%b7%d8%a7%d8%b1%d9%8a%d8%a9-%d8%aa%d9%88%d8%b1%d9%8a%d8%af-%d9%88%d8%aa%d8%b1%d9%83%d9%8a%d8%a8-%d8%a3%d8%ac/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0005/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>توقيع اتفاقيات اطارية توريد وتركيب أجهزة العنايات للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأربعاء 25-05-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الخميس 26-05-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d9%88%d9%82%d9%8a%d8%b9-%d8%a7%d8%aa%d9%81%d8%a7%d9%82%d9%8a%d8%a7%d8%aa-%d8%a7%d8%b7%d8%a7%d8%b1%d9%8a%d8%a9-%d8%aa%d9%88%d8%b1%d9%8a%d8%af-%d8%a3%d8%b3%d8%b1%d8%a9-%d9%88%d8%b7%d8%a7%d9%88/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0006/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>توقيع اتفاقيات اطارية توريد وتركيب أسرة وطاولات فحص للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأحد 15-05-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الإثنين 16-05-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d9%88%d9%82%d9%8a%d8%b9-%d8%a7%d8%aa%d9%81%d8%a7%d9%82%d9%8a%d8%a7%d8%aa-%d8%a7%d8%b7%d8%a7%d8%b1%d9%8a%d8%a9-%d9%84%d8%aa%d9%88%d8%b1%d9%8a%d8%af-%d9%88%d8%aa%d8%b1%d9%83%d9%8a%d8%a8-%d8%a3/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0007/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>توقيع اتفاقيات اطارية لتوريد وتركيب أجهزة الصدمات والعلامات الحيوية للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأحد 29-05-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الإثنين 30-05-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d9%88%d9%82%d9%8a%d8%b9-%d8%a7%d8%aa%d9%81%d8%a7%d9%82%d9%8a%d8%a7%d8%aa-%d8%a7%d8%b7%d8%a7%d8%b1%d9%8a%d8%a9-%d9%84%d8%aa%d9%88%d8%b1%d9%8a%d8%af-%d9%88%d8%aa%d8%b1%d9%83%d9%8a%d8%a8-%d8%a3-2/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0008/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>توقيع اتفاقيات اطارية لتوريد وتركيب أجهزة العمليات للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الإثنين 30-05-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الثلاثاء 31-05-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d9%88%d9%82%d9%8a%d8%b9-%d8%a7%d8%aa%d9%81%d8%a7%d9%82%d9%8a%d8%a7%d8%aa-%d8%a7%d8%b7%d8%a7%d8%b1%d9%8a%d8%a9-%d9%84%d8%aa%d9%88%d8%b1%d9%8a%d8%af-%d9%88%d8%aa%d8%b1%d9%83%d9%8a%d8%a8-%d8%a3-3/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0009/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>توقيع اتفاقيات اطارية لتوريد وتركيب أجهزة التعقيم ومكافحة العدوى للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأحد 22-05-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الإثنين 23-05-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d9%88%d9%82%d9%8a%d8%b9-%d8%a7%d8%aa%d9%81%d8%a7%d9%82%d9%8a%d8%a7%d8%aa-%d8%a7%d8%b7%d8%a7%d8%b1%d9%8a%d8%a9-%d9%84%d8%aa%d9%88%d8%b1%d9%8a%d8%af-%d9%88%d8%aa%d8%b1%d9%83%d9%8a%d8%a8-%d8%a3-4/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0010/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>توقيع اتفاقيات اطارية لتوريد وتركيب أجهزة الرعاية المنزلية للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأحد 19-06-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الإثنين 20-06-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d9%88%d9%82%d9%8a%d8%b9-%d8%a7%d8%aa%d9%81%d8%a7%d9%82%d9%8a%d8%a7%d8%aa-%d8%a7%d8%b7%d8%a7%d8%b1%d9%8a%d8%a9-%d9%84%d8%aa%d9%88%d8%b1%d9%8a%d8%af-%d9%88%d8%aa%d8%b1%d9%83%d9%8a%d8%a8-%d8%a3-5/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0011/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>توقيع اتفاقيات اطارية لتوريد وتركيب أجهزة أمراض الدم للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الإثنين 23-05-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الثلاثاء 24-05-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d9%88%d9%82%d9%8a%d8%b9-%d8%a7%d8%aa%d9%81%d8%a7%d9%82%d9%8a%d8%a7%d8%aa-%d8%a7%d8%b7%d8%a7%d8%b1%d9%8a%d8%a9-%d9%84%d8%aa%d9%88%d8%b1%d9%8a%d8%af-%d9%88%d8%aa%d8%b1%d9%83%d9%8a%d8%a8-%d8%a3-6/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0012/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>توقيع اتفاقيات اطارية لتوريد وتركيب أجهزة مختبرات الكيمياء الحيوية للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الإثنين 20-06-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الثلاثاء 21-06-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d9%88%d9%82%d9%8a%d8%b9-%d8%a7%d8%aa%d9%81%d8%a7%d9%82%d9%8a%d8%a7%d8%aa-%d8%a7%d8%b7%d8%a7%d8%b1%d9%8a%d8%a9-%d9%84%d8%aa%d9%88%d8%b1%d9%8a%d8%af-%d9%88%d8%aa%d8%b1%d9%83%d9%8a%d8%a8-%d8%a3-7/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0013/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>توقيع اتفاقيات اطارية لتوريد وتركيب أجهزة مختبر المناعة للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الثلاثاء 21-06-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الأربعاء 22-06-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d9%88%d9%82%d9%8a%d8%b9-%d8%a7%d8%aa%d9%81%d8%a7%d9%82%d9%8a%d8%a7%d8%aa-%d8%a7%d8%b7%d8%a7%d8%b1%d9%8a%d8%a9-%d9%84%d8%aa%d9%88%d8%b1%d9%8a%d8%af-%d9%88%d8%aa%d8%b1%d9%83%d9%8a%d8%a8-%d8%a3-8/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0014/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>توقيع اتفاقيات اطارية لتوريد وتركيب أجهزة مختبر السموم للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأربعاء 22-06-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الخميس 23-06-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d9%88%d8%b1%d9%8a%d8%af-%d8%a3%d8%ac%d9%87%d8%b2%d8%a9-%d9%85%d9%86%d8%ae%d9%81%d8%b6%d8%a9-%d8%a7%d9%84%d8%aa%d9%83%d9%84%d9%81%d8%a9-%d9%84%d9%84%d8%ac/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0015/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة توريد أجهزة منخفضة التكلفة للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الثلاثاء 31-05-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الأربعاء 01-06-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d8%a7%d9%84%d8%ba%d8%a7%d8%b2%d8%a7%d8%aa-%d8%a7%d9%84%d8%b7%d8%a8%d9%8a%d8%a9-%d8%a7%d9%84%d8%a5%d9%84%d8%ad%d8%a7%d9%82%d9%8a/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0031/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين الغازات الطبية الإلحاقية للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأحد 15-05-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الإثنين 16-05-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%88%d8%aa%d9%88%d8%b1%d9%8a%d8%af-%d8%a3%d8%ac%d9%87%d8%b2%d8%a9-%d9%85%d8%b9-%d9%85%d8%ad%d8%a7%d9%84%d9%8a%d9%84-%d9%88%d9%85-5/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0016/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين وتوريد أجهزة مع محاليل ومستهلكات خاصة بمختبر السموم بنظام القيمة الثابتة لكل نتيجة مؤكدة  GPPRR</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الثلاثاء 10-05-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الأربعاء 11-05-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d9%84%d8%ad%d9%82-%d8%a7%d9%84%d8%a3%d8%af%d9%88%d9%8a%d8%a9-%d8%a7%d9%84%d8%b1%d8%a6%d9%8a%d8%b3%d9%8a%d8%a9-%d8%b1%d9%82%d9%85-2/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0020/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>تأمين ملحق الأدوية الرئيسية رقم (2)</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الخميس 19-05-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الأحد 22-05-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%a7%d9%84%d8%b9%d8%b8%d8%a7%d9%85-%d9%88%d8%a7%d9%84%d8%b9%d9%85%d9%88%d8%af/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0019/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين مستلزمات العظام والعمود الفقري للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الإثنين 16-05-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الثلاثاء 17-05-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d8%a7%d9%84%d8%b9%d9%8a%d9%88%d9%86/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0018/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين مستلزمات العيون للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأربعاء 11-05-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الخميس 12-05-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%ac%d9%87%d9%8a%d8%b2-%d8%ab%d9%84%d8%a7%d8%ac%d8%a7%d8%aa-%d8%a7%d9%84%d9%85%d9%88%d8%aa%d9%89-%d9%84%d9%84%d8%ac%d9%87%d8%a7%d8%aa-%d8%a7%d9%84%d8%b5/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0036/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تجهيز ثلاجات الموتى للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الثلاثاء 14-06-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الأربعاء 15-06-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d9%88%d9%82%d9%8a%d8%b9-%d8%a7%d8%aa%d9%81%d8%a7%d9%82%d9%8a%d8%a7%d8%aa-%d8%a7%d8%b7%d8%a7%d8%b1%d9%8a%d8%a9-%d9%84%d8%aa%d9%88%d8%b1%d9%8a%d8%af-%d9%88%d8%aa%d8%b1%d9%83%d9%8a%d8%a8-%d8%a3-9/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0025/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>توقيع اتفاقيات اطارية لتوريد وتركيب أجهزة المثاقيب الجراحية للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأربعاء 08-06-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الخميس 09-06-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d9%88%d9%82%d9%8a%d8%b9-%d8%a7%d8%aa%d9%81%d8%a7%d9%82%d9%8a%d8%a7%d8%aa-%d8%a7%d8%b7%d8%a7%d8%b1%d9%8a%d8%a9-%d9%84%d8%aa%d9%88%d8%b1%d9%8a%d8%af-%d9%88%d8%aa%d8%b1%d9%83%d9%8a%d8%a8-%d8%a3-10/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0023/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>توقيع اتفاقيات اطارية لتوريد وتركيب أجهزة الليزر للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الثلاثاء 07-06-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الأربعاء 08-06-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d9%88%d9%82%d9%8a%d8%b9-%d8%a7%d8%aa%d9%81%d8%a7%d9%82%d9%8a%d8%a7%d8%aa-%d8%a7%d8%b7%d8%a7%d8%b1%d9%8a%d8%a9-%d9%84%d8%aa%d9%88%d8%b1%d9%8a%d8%af-%d9%88%d8%aa%d8%b1%d9%83%d9%8a%d8%a8-%d8%a3-11/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0021/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>توقيع اتفاقيات اطارية لتوريد وتركيب أجهزة مختبر فحص نقطة الرعاية للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأحد 05-06-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الإثنين 06-06-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d9%88%d9%82%d9%8a%d8%b9-%d8%a7%d8%aa%d9%81%d8%a7%d9%82%d9%8a%d8%a7%d8%aa-%d8%a7%d8%b7%d8%a7%d8%b1%d9%8a%d8%a9-%d9%84%d8%aa%d8%ac%d9%87%d9%8a%d8%b2-%d8%b3%d9%8a%d8%a7%d8%b1%d8%a7%d8%aa-%d8%a7/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0022/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>توقيع اتفاقيات اطارية لتجهيز سيارات الإسعاف للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الإثنين 06-06-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الثلاثاء 07-06-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d9%88%d8%b1%d9%8a%d8%af-%d9%88-%d8%aa%d8%b1%d9%83%d9%8a%d8%a8-%d8%a3%d8%ac%d9%87%d8%b2%d8%a9-%d8%a7%d9%84%d9%81%d8%ad%d8%b5-%d9%88-%d8%a7%d9%84%d9%85%d8%b9/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0026/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة توريد و تركيب أجهزة الفحص و المعايرة والمحاكاة للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأحد 12-06-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الإثنين 13-06-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d9%88%d9%82%d9%8a%d8%b9-%d8%a7%d8%aa%d9%81%d8%a7%d9%82%d9%8a%d8%a7%d8%aa-%d8%a7%d8%b7%d8%a7%d8%b1%d9%8a%d8%a9-%d9%84%d8%aa%d9%88%d8%b1%d9%8a%d8%af-%d9%88-%d8%aa%d8%b1%d9%83%d9%8a%d8%a8-%d8%a3/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0027/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>توقيع اتفاقيات اطارية لتوريد و تركيب أجهزة عيادات الأنف و الأذن و الحنجرة للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الإثنين 13-06-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الثلاثاء 14-06-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d9%88%d9%82%d9%8a%d8%b9-%d8%a7%d8%aa%d9%81%d8%a7%d9%82%d9%8a%d8%a7%d8%aa-%d8%a7%d8%b7%d8%a7%d8%b1%d9%8a%d8%a9-%d9%84%d8%aa%d9%88%d8%b1%d9%8a%d8%af-%d9%88-%d8%aa%d8%b1%d9%83%d9%8a%d8%a8-%d8%a3-2/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0042/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>توقيع اتفاقيات اطارية لتوريد و تركيب أجهزة مختبر بنك الدم للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الإثنين 27-06-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الثلاثاء 28-06-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%a7%d9%84%d8%b9%d9%82%d9%85-%d9%88%d8%a7%d9%84%d8%a5%d8%ae%d8%b5%d8%a7%d8%a8/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0033/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين مستلزمات العقم والإخصاب للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الثلاثاء 17-05-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الأربعاء 18-05-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%a7%d9%84%d8%a7%d8%ad%d8%aa%d9%8a%d8%a7%d8%ac%d8%a7%d8%aa-%d8%a7%d9%84%d8%aa/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0030/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين مستلزمات الاحتياجات التعليمية للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الخميس 26-05-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الأحد 29-05-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%84%d8%ad%d9%82-%d8%a3%d8%ac%d9%87%d8%b2%d8%a9-%d8%b7%d8%a8%d9%8a%d8%a9-%d8%b9%d8%a7%d9%85%d8%a9-%d8%b1%d9%82%d9%85-1-%d9%84%d9%84%d8%ac%d9%87%d8%a7%d8%aa-%d8%a7%d9%84%d8%b5%d8%ad%d9%8a/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0028/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>ملحق أجهزة طبية عامة رقم (1) للجهات الصحية الحكومية لعام 2022 م</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأربعاء 15-06-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الخميس 16-06-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d8%a7%d9%84%d9%86%d8%b8%d8%a7%d8%a6%d8%b1-%d8%a7%d9%84%d9%85%d8%b4%d8%b9%d8%a9-%d9%88%d8%b5%d8%a8%d8%ba%d8%a7%d8%aa-%d8%a7%d9%84%d8%a3%d8%b4%d8%b9%d8%a9/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0034/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>تأمين النظائر المشعة وصبغات الأشعة</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الخميس 02-06-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الأحد 05-06-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%ad%d8%a7%d9%84%d9%8a%d9%84-%d9%88%d8%a3%d8%af%d9%88%d9%8a%d8%a9-%d8%a7%d9%84%d8%aa%d8%ba%d8%b0%d9%8a%d8%a9-%d8%a7%d9%84%d9%88%d8%b1%d9%8a%d8%af%d9%8a%d8%a9/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0035/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>تأمين محاليل وأدوية التغذية الوريدية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الخميس 16-06-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الأحد 19-06-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%ad%d8%a7%d9%84%d9%8a%d9%84-%d9%88%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d9%85%d8%ae%d8%aa%d8%a8%d8%b1%d8%a7/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0032/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين محاليل ومستلزمات مختبرات الأبحاث الإلحاقية للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الثلاثاء 28-06-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الأربعاء 29-06-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%a7%d9%84%d8%b9%d9%84%d8%a7%d8%ac-%d8%a7%d9%84%d8%aa%d9%86%d9%81%d8%b3%d9%8a/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0029/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين مستلزمات العلاج التنفسي والتخدير للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الخميس 09-06-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الأحد 12-06-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%a7%d9%84%d8%ac%d9%84%d8%af%d9%8a%d8%a9-%d9%84%d9%84%d8%ac%d9%87%d8%a7%d8%aa/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0044/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين مستلزمات الجلدية للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الخميس 23-06-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الأحد 26-06-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d9%88%d9%82%d9%8a%d8%b9-%d8%a7%d8%aa%d9%81%d8%a7%d9%82%d9%8a%d8%a7%d8%aa-%d8%a7%d8%b7%d8%a7%d8%b1%d9%8a%d8%a9-%d9%84%d8%aa%d9%88%d8%b1%d9%8a%d8%af-%d9%88/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0037/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة توقيع اتفاقيات اطارية لتوريد وتركيب أجهزة المختبر العام للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأحد 17-07-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الإثنين 18-07-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d9%88%d9%82%d9%8a%d8%b9-%d8%a7%d8%aa%d9%81%d8%a7%d9%82%d9%8a%d8%a7%d8%aa-%d8%a7%d8%b7%d8%a7%d8%b1%d9%8a%d8%a9-%d9%84%d8%aa%d9%88%d8%b1%d9%8a%d8%af-%d9%88-2/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0038/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة توقيع اتفاقيات اطارية لتوريد وتركيب أجهزة المختبر الوراثية للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الإثنين 18-07-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الثلاثاء 19-07-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d9%88%d9%82%d9%8a%d8%b9-%d8%a7%d8%aa%d9%81%d8%a7%d9%82%d9%8a%d8%a7%d8%aa-%d8%a7%d8%b7%d8%a7%d8%b1%d9%8a%d8%a9-%d9%84%d8%aa%d9%88%d8%b1%d9%8a%d8%af-%d9%88%d8%aa%d8%b1%d9%83%d9%8a%d8%a8-%d8%a3-12/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0039/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>توقيع اتفاقيات اطارية لتوريد وتركيب أجهزة المختبر التشريحي للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الثلاثاء 19-07-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الأربعاء 20-07-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d9%88%d9%82%d9%8a%d8%b9-%d8%a7%d8%aa%d9%81%d8%a7%d9%82%d9%8a%d8%a7%d8%aa-%d8%a7%d8%b7%d8%a7%d8%b1%d9%8a%d8%a9-%d9%84%d8%aa%d9%88%d8%b1%d9%8a%d8%af-%d9%88%d8%aa%d8%b1%d9%83%d9%8a%d8%a8-%d8%a3-13/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0040/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>توقيع اتفاقيات اطارية لتوريد وتركيب أجهزة مختبر الأحياء الدقيقة للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأربعاء 20-07-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الخميس 21-07-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d9%88%d9%82%d9%8a%d8%b9-%d8%a7%d8%aa%d9%81%d8%a7%d9%82%d9%8a%d8%a7%d8%aa-%d8%a7%d8%b7%d8%a7%d8%b1%d9%8a%d8%a9-%d9%84%d8%aa%d9%88%d8%b1%d9%8a%d8%af-%d9%88%d8%aa%d8%b1%d9%83%d9%8a%d8%a8-%d8%a3-14/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0041/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>توقيع اتفاقيات اطارية لتوريد وتركيب أجهزة مختبر العقم والأخصاب للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأحد 24-07-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الإثنين 25-07-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d8%a3%d8%ac%d9%87%d8%b2%d8%a9-%d9%85%d8%ae%d8%aa%d8%a8%d8%b1-%d8%a7%d9%84%d8%ae%d9%84%d8%a7%d9%8a%d8%a7-%d8%a7%d9%84%d8%ac%d8%b0/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0043/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين أجهزة مختبر الخلايا الجذعية للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الإثنين 25-07-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الثلاثاء 26-07-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d9%81%d8%ad%d9%88%d8%b5%d8%a7%d8%aa-%d9%86%d9%82%d8%a7%d8%b7-%d8%a7%d9%84%d8%b1/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0047/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين مستلزمات فحوصات نقاط الرعاية POCT &#8211; GPPRR  للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الخميس 21-07-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الأحد 24-07-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%a7%d8%a3%d9%84%d8%b3%d9%86%d8%a7%d9%86-%d8%a7%d9%84%d8%b9%d8%a7%d9%85%d8%a9/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0049/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين مستلزمات الأسنان &#8211; العامة للجهات  الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأربعاء 27-07-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الخميس 28-07-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%a7%d9%84%d9%85%d8%b9%d9%82%d9%85%d8%a7%d8%aa-%d9%84%d9%84%d8%ac%d9%87%d8%a7/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0056/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين مستلزمات المعقمات للجهات الصحية  الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأربعاء 29-06-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الخميس 30-06-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%b7%d8%a8%d9%8a%d8%a9-%d8%b9%d8%a7%d9%85%d8%a9-%d8%aa%d9%85%d8%b1%d9%8a%d8%b6/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0017/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين مستلزمات طبية عامة (تمريض ووحدة الحروق) للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الإثنين 06-06-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الثلاثاء 07-06-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%a7%d9%84%d8%a3%d8%b4%d8%b9%d8%a9-%d8%a7%d9%84%d8%aa%d8%af%d8%a7%d8%ae%d9%84/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0051/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين مستلزمات الأشعة التداخلية وقسطرة القلب للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأحد 26-06-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الإثنين 27-06-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%a7%d9%84%d8%ba%d8%b3%d9%8a%d9%84-%d8%a7%d9%84%d9%83%d9%84%d9%88%d9%8a-%d9%84/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0048/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين مستلزمات الغسيل الكلوي للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الثلاثاء 26-07-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الأربعاء 27-07-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d8%a7%d9%84%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%a7%d9%84%d8%b9%d8%a7%d9%85%d8%a9-%d8%a7%d9%84%d8%ac%d8%b1%d8%a7/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0045/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين المستلزمات العامة الجراحية للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الخميس 28-07-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الأحد 31-07-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%a7%d9%84%d8%a3%d8%b0%d9%86-%d9%88%d8%a7%d9%84%d8%a3%d9%86%d9%81-%d9%88%d8%a7/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0046/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين مستلزمات الأذن والأنف والحنجرة الإلحاقية للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأحد 31-07-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الإثنين 01-08-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%a7%d9%84%d8%a3%d8%b7%d8%b1%d8%a7%d9%81-%d8%a7%d9%84%d8%b5%d9%86%d8%a7%d8%b9/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0050/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين مستلزمات الأطراف الصناعية للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأربعاء 17-08-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الخميس 18-08-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%a7%d9%84%d8%aa%d8%b9%d9%82%d9%8a%d9%85-%d9%84%d9%84%d8%ac%d9%87%d8%a7%d8%aa/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0053/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين مستلزمات التعقيم للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الإثنين 08-08-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الثلاثاء 09-08-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d9%88%d9%82%d9%8a%d8%b9-%d8%a7%d8%aa%d9%81%d8%a7%d9%82%d9%8a%d8%a7%d8%aa-%d8%a7%d8%b7%d8%a7%d8%b1%d9%8a%d8%a9-%d9%84%d8%aa%d9%88%d8%b1%d9%8a%d8%af-%d9%88%d8%aa%d8%b1%d9%83%d9%8a%d8%a8-%d8%a3-15/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0024/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>توقيع اتفاقيات اطارية لتوريد وتركيب أجهزة العيون للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأربعاء 24-08-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الخميس 25-08-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d9%88%d9%85%d8%ad%d8%a7%d9%84%d9%8a%d9%84-%d8%a7%d9%84%d9%85%d8%ae%d8%aa%d8%a8-2/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0061/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين مستلزمات ومحاليل المختبرات &#8211; المرحلة الأولى  &#8211; للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الإثنين 26-09-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الثلاثاء 27-09-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%a7%d9%84%d8%a3%d8%b3%d9%86%d8%a7%d9%86-%d8%a7%d9%84%d9%85%d8%ae%d8%aa%d8%a8/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0058/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين مستلزمات الأسنان ( المختبر والزراعة وجراحة الوجه والفكين ) للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الخميس 15-09-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الأحد 18-09-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%84%d8%ad%d9%82-%d8%a3%d8%ac%d9%87%d8%b2%d8%a9-%d8%b7%d8%a8%d9%8a%d8%a9-%d8%b9%d8%a7%d9%85%d8%a9-%d8%b1%d9%82%d9%85-2-%d9%84%d9%84%d8%ac%d9%87%d8%a7%d8%aa-%d8%a7%d9%84%d8%b5%d8%ad%d9%8a/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0052/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>ملحق أجهزة طبية عامة رقم ( 2 ) للجهات الصحية الحكومية لعام ٢٠٢٢ م</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الإثنين 05-09-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الثلاثاء 06-09-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d9%81%d8%ad%d9%88%d8%b5%d8%a7%d8%aa-%d8%ad%d8%af%d9%8a%d8%ab%d9%8a-%d8%a7%d9%84/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0054/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين مستلزمات  فحوصات حديثي الولادة NBS &#8211; GPPRR للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الثلاثاء 20-09-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الأربعاء 21-09-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%ac%d8%b1%d8%a7%d8%ad%d8%a9-%d8%a7%d9%84%d9%82%d9%84%d8%a8-%d9%88%d8%a7%d9%84/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0062/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين مستلزمات جراحة القلب والأوعية الدموية للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأربعاء 07-09-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الخميس 08-09-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d8%a7%d9%84%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%a7%d9%84%d8%b9%d8%a7%d9%85%d8%a9-%d8%a7%d9%84%d8%ae%d9%8a%d9%88/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0055/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين المستلزمات العامة ( الخيوط الجراحية والمناظير الباطنية والجراح الآلي ) للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأحد 11-09-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الإثنين 12-09-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%a7%d9%84%d8%aa%d8%a3%d9%87%d9%8a%d9%84-%d9%88%d8%a7%d9%84%d8%b9%d9%84%d8%a7/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0059/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين مستلزمات التأهيل والعلاج الطبيعي للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأربعاء 19-10-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الخميس 20-10-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%a7%d9%84%d9%85%d9%86%d8%a7%d8%b8%d9%8a%d8%b1-%d9%84%d9%84%d8%ac%d9%87%d8%a7/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0060/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين مستلزمات المناظير للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الثلاثاء 27-09-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الأربعاء 28-09-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d8%a7%d9%84%d9%84%d9%82%d8%a7%d8%ad%d8%a7%d8%aa-%d8%a7%d9%84%d8%b1%d8%a6%d9%8a%d8%b3%d9%8a%d8%a9-%d9%84%d9%84%d8%ac%d9%87%d8%a7%d8%aa-%d8%a7%d9%84%d8%b5%d8%ad%d9%8a-2/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0064/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>تأمين اللقاحات الرئيسية للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الإثنين 14-11-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الثلاثاء 15-11-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%a7%d9%84%d8%a3%d8%af%d9%88%d8%a7%d8%aa-%d8%a7%d9%84%d8%ac%d8%b1%d8%a7%d8%ad%d9%8a%d8%a9-%d8%a7%d9%84%d8%aa%d8%ae/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0063/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>تأمين مستلزمات الأدوات الجراحية التخصصية وأدوات المناظير للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأربعاء 09-11-2022</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الخميس 10-11-2022</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%88%d8%aa%d9%88%d8%b1%d9%8a%d8%af-%d8%a3%d8%ac%d9%87%d8%b2%d8%a9-%d9%85%d8%b9-%d9%85%d8%ad%d8%a7%d9%84%d9%8a%d9%84-%d9%88%d9%85%d8%b3%d8%aa%d9%87%d9%84%d9%83%d8%a7/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0057/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>تأمين وتوريد أجهزة مع محاليل ومستهلكات خاصة بالمختبرات العامة والسموم بنظام القيمة الثابتة لكل نتيجة مؤكدة GPPRR</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الثلاثاء 10-01-2023</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الأربعاء 11-01-2023</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%ad%d8%a7%d9%84%d9%8a%d9%84-%d9%88%d9%85%d8%b3%d8%aa%d9%87%d9%84%d9%83%d8%a7%d8%aa-%d8%a7%d9%84%d9%85%d8%ae%d8%aa%d8%a8/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0069/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين محاليل ومستهلكات المختبرات مع توريد أجهزة لأقسام علم أمراض الأنسجة وعلم الخلية والتدفق الخلوي بنظام القيمة الثابتة لكل نتيجة مؤكدة GPPRR</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأحد 15-01-2023</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الإثنين 16-01-2023</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%ad%d8%a7%d9%84%d9%8a%d9%84-%d9%88%d9%85%d8%b3%d8%aa%d9%87%d9%84%d9%83%d8%a7%d8%aa-%d8%a7%d9%84%d9%85%d8%ae%d8%aa%d8%a8-2/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0068/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين محاليل ومستهلكات المختبرات مع توريد أجهزة لأقسام بنوك الدم وعلم المناعة والأحياء الدقيقة و الجزيئية بنظام القيمة الثابتة لكل نتيجة مؤكدة GPPRR</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأربعاء 01-02-2023</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الخميس 02-02-2023</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%84%d8%ad%d9%82-%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%a7%d9%84%d8%af%d9%84%d9%8a%d9%84-%d8%a7%d9%84%d9%85%d9%88%d8%ad%d8%af-%d9%84%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0003/23</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>ملحق منافسة الدليل الموحد لتأمين مستلزمات ومحاليل المختبرات العامة (مُلحق المرحلة الأولى) للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الثلاثاء 07-03-2023</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الأربعاء 08-03-2023</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d8%a7%d9%84%d9%81%d9%8a%d8%aa%d8%a7%d9%85%d9%8a%d9%86%d8%a7%d8%aa-%d9%88%d8%a7%d9%84%d9%85%d8%b9%d8%a7%d8%af%d9%86-%d9%84%d9%84/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0070/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين الفيتامينات والمعادن للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأربعاء 15-03-2023</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الخميس 16-03-2023</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d8%a7%d9%84%d8%a3%d8%af%d9%88%d9%8a%d8%a9-%d8%a7%d9%84%d8%b1%d8%a6%d9%8a%d8%b3%d9%8a%d8%a9-%d9%84%d9%84%d8%ac%d9%87%d8%a7%d8%aa/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0066/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين الأدوية الرئيسية للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأربعاء 17-05-2023</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الخميس 18-05-2023</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d8%a8%d9%86%d8%af-%d9%84%d9%82%d8%a7%d8%ad-%d9%84%d8%b5%d8%a7%d9%84%d8%ad-%d9%88%d8%b2%d8%a7%d8%b1%d8%a9-%d8%a7%d9%84%d8%b5%d8%ad/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0038/23</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين بند لقاح لصالح وزارة الصحة</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأحد 02-04-2023</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الإثنين 03-04-2023</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%84%d8%ad%d9%82-%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%a7%d9%84%d8%b9%d9%84%d8%a7%d8%ac-%d8%a7%d9%84%d8%aa%d9%86%d9%81%d8%b3%d9%8a-%d9%88/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0002/23 </p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>ملحق منافسة مستلزمات العلاج التنفسي والتخدير للجهات الصحية الحكومية رقم NPT0002/23</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الثلاثاء 09-05-2023</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الأربعاء 10-05-2023</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%84%d8%ad%d9%82-%d8%a7%d9%84%d8%a5%d8%aa%d9%81%d8%a7%d9%82%d9%8a%d8%a7%d8%aa-%d8%a7%d9%84%d8%a5%d8%b7%d8%a7%d8%b1%d9%8a%d8%a9-%d9%84%d8%aa%d9%88%d8%b1%d9%8a%d8%af-%d9%88%d8%aa%d8%b1%d9%83/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0004/23</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>ملحق الإتفاقيات الإطارية لتوريد وتركيب أجهزة طبية للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأحد 07-05-2023</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الإثنين 08-05-2023</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d8%a3%d8%af%d9%88%d9%8a%d8%a9-%d8%ae%d8%af%d9%85%d8%a9-%d9%88%d8%b5%d9%81%d8%aa%d9%8a/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0067/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>تأمين أدوية خدمة وصفتي</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الثلاثاء 23-05-2023</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الأربعاء 24-05-2023</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%88%d8%aa%d9%88%d8%b1%d9%8a%d8%af-%d8%a3%d8%ac%d9%87%d8%b2%d8%a9-%d9%85%d8%b9-%d9%85%d8%ad%d8%a7%d9%84%d9%8a%d9%84-%d9%88%d9%85-7/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0007/23</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين وتوريد أجهزة مع محاليل ومستهلكات خاصة بنقاط الرعاية (POCT) بنظام القيمة الثابتة لكل نتيجة مؤكدة GPPRR</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الثلاثاء 16-05-2023</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الأربعاء 17-05-2023</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d8%a8%d9%86%d9%88%d8%af-%d8%a7%d9%84%d9%83%d9%8a%d9%85%d8%a7%d9%88%d9%8a%d8%a7%d8%aa-%d9%84%d9%84%d8%ac%d9%87%d8%a7%d8%aa-%d8%a7/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0005/23</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين بنود الكيماويات للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الإثنين 15-05-2023</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الثلاثاء 16-05-2023</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%84%d8%ad%d9%82-%d8%a7%d9%84%d8%a3%d8%ac%d9%87%d8%b2%d8%a9-%d8%a7%d9%84%d8%b7%d8%a8%d9%8a%d8%a9-%d8%b1%d9%82%d9%85-1/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0006/23</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>ملحق الأجهزة الطبية رقم (1)</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأحد 11-06-2023</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الإثنين 12-06-2023</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%a7%d9%84%d8%aa%d8%a3%d9%87%d9%8a%d9%84-%d9%88%d8%a7%d9%84%d8%b9%d9%84%d8%a7-2-3/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0009/23</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين مستلزمات التأهيل والعلاج الطبيعي (الإلحاقية) للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الإثنين 22-05-2023</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الثلاثاء 23-05-2023</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%a7%d9%84%d8%aa%d8%b9%d9%82%d9%8a%d9%85-%d8%a7%d9%84%d8%a5%d9%84%d8%ad%d8%a7/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0008/23</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين مستلزمات التعقيم الإلحاقية للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأربعاء 31-05-2023</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الخميس 01-06-2023</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d8%a3%d8%af%d9%88%d9%8a%d8%a9-%d8%ae%d8%a7%d8%b5%d8%a9-%d9%84%d9%84%d8%ac%d9%87%d8%a7%d8%aa-%d8%a7%d9%84%d8%b5%d8%ad%d9%8a%d8%a9/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0072/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين أدوية خاصة للجهات الصحية الحكومية (المرحلة الثانية)</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الإثنين 12-06-2023</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الثلاثاء 13-06-2023</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d8%a3%d8%af%d9%88%d9%8a%d8%a9-%d8%ae%d8%a7%d8%b5%d8%a9-%d9%84%d9%84%d8%ac%d9%87%d8%a7%d8%aa-%d8%a7%d9%84%d8%b5%d8%ad%d9%8a%d8%a9-2/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0071/22</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين أدوية خاصة للجهات الصحية الحكومية (المرحلة الأولى)</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الثلاثاء 13-06-2023</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الأربعاء 14-06-2023</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d8%a3%d8%af%d9%88%d9%8a%d8%a9-%d8%ae%d8%a7%d8%b5%d8%a9-%d9%84%d9%84%d8%ac%d9%87%d8%a7%d8%aa-%d8%a7%d9%84%d8%b5%d8%ad%d9%8a%d8%a9-%d8%a7%d9%84%d8%ad%d9%83%d9%88%d9%85/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0040/23</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>تأمين أدوية خاصة للجهات الصحية الحكومية (المرحلة الثالثة)</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأحد 04-06-2023</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الإثنين 05-06-2023</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%a7%d9%84%d8%af%d9%84%d9%8a%d9%84-%d8%a7%d9%84%d9%85%d9%88%d8%ad%d8%af-%d9%84%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0012/23</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة الدليل الموحد لتأمين مستلزمات ومحاليل المختبرات العامة (المرحلة الثانية) للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأحد 28-05-2023</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الإثنين 29-05-2023</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%a7%d9%84%d8%b9%d9%84%d9%88%d9%85-%d8%a7%d9%84%d8%b9%d8%b5%d8%a8%d9%8a%d8%a9/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0011/23</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين مستلزمات العلوم العصبية (جراحة المخ والأعصاب، الأشعة التداخلية العصبية، فيسيولوجية الأعصاب ، ومستلزمات التحفيز العصبي ) للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأربعاء 14-06-2023</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الخميس 15-06-2023</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d9%88%d9%82%d9%8a%d8%b9-%d8%a7%d8%aa%d9%81%d8%a7%d9%82%d9%8a%d8%a7%d8%aa-%d8%a7%d8%b7%d8%a7%d8%b1%d9%8a%d8%a9-%d9%84%d8%aa%d9%88%d8%b1%d9%8a%d8%af-%d9%88%d8%aa%d8%b1%d9%83%d9%8a%d8%a8-%d8%a3-16/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0010/23</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>توقيع اتفاقيات اطارية لتوريد وتركيب أجهزة التصوير الطبي للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأحد 23-07-2023</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الإثنين 24-07-2023</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d9%88%d9%82%d9%8a%d8%b9-%d8%a7%d8%aa%d9%81%d8%a7%d9%82%d9%8a%d8%a7%d8%aa-%d8%a7%d8%b7%d8%a7%d8%b1%d9%8a%d8%a9-%d9%84%d8%aa%d9%88%d8%b1%d9%8a%d8%af-%d8%a3%d8%ac%d9%87%d8%b2%d8%a9-%d8%a7%d9%84-3/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0014/23</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>توقيع اتفاقيات اطارية لتوريد أجهزة التأهيل الطبي</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الثلاثاء 25-07-2023</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الأربعاء 26-07-2023</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%a7%d9%84%d8%a3%d8%b7%d8%b1%d8%a7%d9%81-%d8%a7%d9%84%d8%b5%d9%86%d8%a7%d8%b9%d9%8a%d8%a9-%d8%a7%d9%84%d8%a5/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0017/23</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة مستلزمات الأطراف الصناعية الإلحاقية للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأربعاء 26-07-2023</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الخميس 27-07-2023</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%a7%d9%84%d8%a3%d8%b3%d9%86%d8%a7%d9%86-%d8%a7%d9%84%d8%a5%d9%84%d8%ad%d8%a7/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0016/23</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين مستلزمات الأسنان الإلحاقية للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأحد 30-07-2023</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الإثنين 31-07-2023</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%a7%d9%84%d8%a3%d9%86%d9%81-%d9%88%d8%a7%d9%84%d8%a3%d8%b0%d9%86-%d9%88%d8%a7-2/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0015/23</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين مستلزمات الأنف والأذن والحنجرة  للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأحد 06-08-2023</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الإثنين 07-08-2023</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d9%88%d9%82%d9%8a%d8%b9-%d8%a7%d8%aa%d9%81%d8%a7%d9%82%d9%8a%d8%a7%d8%aa-%d8%a7%d8%b7%d8%a7%d8%b1%d9%8a%d8%a9-%d9%84%d8%aa%d9%88%d8%b1%d9%8a%d8%af-%d8%a3-2/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0013/23</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة توقيع اتفاقيات اطارية لتوريد أجهزة المختبرات التخصصية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأحد 20-08-2023</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الإثنين 21-08-2023</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d9%88%d9%82%d9%8a%d8%b9-%d8%a7%d8%aa%d9%81%d8%a7%d9%82%d9%8a%d8%a7%d8%aa-%d8%a7%d8%b7%d8%a7%d8%b1%d9%8a%d8%a9-%d9%84%d8%aa%d9%88%d8%b1%d9%8a%d8%af-%d9%88-3/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0020/23</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة توقيع اتفاقيات اطارية لتوريد وتركيب أجهزة المختبر العام</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الثلاثاء 15-08-2023</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الأربعاء 16-08-2023</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d9%88%d9%82%d9%8a%d8%b9-%d8%a7%d8%aa%d9%81%d8%a7%d9%82%d9%8a%d8%a7%d8%aa-%d8%a7%d8%b7%d8%a7%d8%b1%d9%8a%d8%a9-%d9%84%d8%aa%d9%88%d8%b1%d9%8a%d8%af-%d9%88-4/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0019/23</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة توقيع اتفاقيات اطارية لتوريد وتركيب أجهزة طبية للجهات الصحية الحكومية &#8211; ملحق 2</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الإثنين 14-08-2023</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الثلاثاء 15-08-2023</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d8%a8%d9%86%d8%af-%d9%84%d9%82%d8%a7%d8%ad-%d9%84%d8%b5%d8%a7%d9%84%d8%ad-%d9%88%d8%b2%d8%a7%d8%b1%d8%a9-%d8%a7%d9%84%d8%b5%d8%ad-2/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0041/23</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين بند لقاح لصالح وزارة الصحة (المرحلة الثانية)</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأربعاء 12-07-2023</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الخميس 13-07-2023</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%a7%d9%84%d9%85%d9%86%d8%a7%d8%b8%d9%8a%d8%b1-%d8%a7%d9%84%d8%a5%d9%84%d8%ad%d8%a7%d9%82%d9%8a%d8%a9-%d9%84/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0022/23</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة مستلزمات المناظير الإلحاقية للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الثلاثاء 01-08-2023</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الأربعاء 02-08-2023</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%a7%d9%84%d9%85%d8%b9%d9%82%d9%85%d8%a7%d8%aa-%d8%a7%d9%84%d8%a5%d9%84%d8%ad/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0024/23</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين مستلزمات المعقمات الإلحاقية للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الإثنين 07-08-2023</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الثلاثاء 08-08-2023</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d8%a7%d9%84%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%a7%d9%84%d8%b7%d8%a8%d9%8a%d8%a9-%d8%a7%d9%84%d8%a5%d9%84%d8%ad/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0023/23</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين المستلزمات الطبية الإلحاقية (تمريض ووحدة الحروق)</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الثلاثاء 12-09-2023</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الأربعاء 13-09-2023</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b4%d8%aa%d9%82%d8%a7%d8%aa-%d8%a7%d9%84%d8%af%d9%85-%d9%84%d9%84%d8%ac%d9%87%d8%a7%d8%aa-%d8%a7%d9%84%d8%b5%d8%ad%d9%8a%d8%a9-%d8%a7%d9%84%d8%ad%d9%83%d9%88/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0025/23</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>تأمين مشتقات الدم للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأربعاء 27-09-2023</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الخميس 28-09-2023</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%ac%d9%87%d9%8a%d8%b2-%d9%88%d8%aa%d9%88%d8%b1%d9%8a%d8%af-%d8%b3%d9%8a%d8%a7%d8%b1%d8%a7%d8%aa-%d8%a5%d8%b3%d8%b9%d8%a7%d9%81-%d9%84%d9%84%d8%ac%d9%87/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0043/23</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تجهيز وتوريد سيارات إسعاف للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الثلاثاء 26-09-2023</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الأربعاء 27-09-2023</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%a7%d9%84%d8%a3%d8%b4%d8%b9%d8%a9-%d8%a7%d9%84%d8%aa%d8%af%d8%a7%d8%ae%d9%84-2/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0027/23</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين مستلزمات الأشعة التداخلية وقسطرة القلب الإلحاقية للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الثلاثاء 03-10-2023</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الأربعاء 04-10-2023</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%a7%d9%84%d8%af%d9%84%d9%8a%d9%84-%d8%a7%d9%84%d9%85%d9%88%d8%ad%d8%af-%d9%84%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-2/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0026/23</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة الدليل الموحد لتأمين مستلزمات ومحاليل المختبرات العامة (المرحلة الثالثة) للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأحد 15-10-2023</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الإثنين 16-10-2023</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d8%a7%d9%84%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%a7%d9%84%d8%b9%d8%a7%d9%85%d8%a9-%d8%a7%d9%84%d8%ac%d8%b1%d8%a7%d8%ad%d9%8a%d8%a9-%d9%85%d8%b3%d8%a7/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0029/23</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين المستلزمات العامة الجراحية (مسالك بولية،والجراحة) الإلحاقية للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الثلاثاء 10-10-2023</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الأربعاء 11-10-2023</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%a7%d9%84%d8%b9%d9%8a%d9%88%d9%86-%d8%a7%d9%84%d8%a5%d9%84%d8%ad%d8%a7%d9%82/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0030/23</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين مستلزمات العيون الإلحاقية للجهات الصحية الحكومية رقم NPT0030/23</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الثلاثاء 17-10-2023</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الأربعاء 18-10-2023</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/19580-2/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0018/23</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين ملحق الأدوية الرئيسية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأحد 08-10-2023</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الإثنين 09-10-2023</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d8%a7%d9%84%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%a7%d9%84%d8%b9%d8%a7%d9%85%d8%a9-%d8%a7%d9%84%d8%ae%d9%8a%d9%88-2/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0034/23</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين المستلزمات العامة (الخيوط الجراحية والمناظير الباطنية &#8211; والجراح الآلي) الإلحاقية للجهات الصحية الحكومية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأربعاء 29-11-2023</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الخميس 30-11-2023</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%a7%d9%84%d8%a3%d8%b3%d9%86%d8%a7%d9%86-%d8%a7%d9%84%d9%85%d8%ae%d8%aa%d8%a8-2/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0031/23</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين مستلزمات الأسنان  (المختبر والزراعة وجراحة الوجة والفكين) الإلحاقية   رقم NPT0031/23</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الثلاثاء 05-12-2023</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الأربعاء 06-12-2023</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%88%d8%aa%d9%88%d8%b1%d9%8a%d8%af-%d9%85%d8%ad%d8%a7%d9%84%d9%8a%d9%84-%d9%88%d9%85%d8%b3%d8%aa%d9%87%d9%84%d9%83%d8%a7%d8%aa/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0032/23</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين وتوريد محاليل ومستهلكات خاصة بالتدفق الخلوي والتطابق النسيجي والجينات مع الأجهزة بنظام اتفاقية محاليل مقابل أجهزة (Reagent deal)</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأربعاء 20-12-2023</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الخميس 21-12-2023</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%b3%d8%aa%d9%84%d8%b2%d9%85%d8%a7%d8%aa-%d8%ac%d8%b1%d8%a7%d8%ad%d8%a9-%d8%a7%d9%84%d9%82%d9%84%d8%a8-%d9%88%d8%a7%d9%84-2/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0033/23</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين مستلزمات جراحة القلب والأوعية الدموية الإلحاقية</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الأربعاء 06-12-2023</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الخميس 07-12-2023</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


        

 
                    <style type="text/css">
                    	.filter-tabs li.active.the-final-results{background: #a3b34b;}
                    </style>
                    <div class="column-box mix Tender_width  the-final-results1" data-myorder="40" style="background: rgba(163, 179, 75,0.8);">



                    	<div class="box"> 

                                                  <a href="https://www.nupco.com/tenders_post/%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a9-%d8%aa%d8%a3%d9%85%d9%8a%d9%86-%d9%85%d8%ad%d8%a7%d9%84%d9%8a%d9%84-%d9%88%d9%85%d8%b3%d8%aa%d9%87%d9%84%d9%83%d8%a7%d8%aa-%d9%85%d9%82%d8%a7%d8%a8%d9%84-%d8%aa/" style="color:#fff!important">
                    	 <div class="box box_arbic">
                    	    <div class="box_arbic_col">
                    	    	<div class="box_arbic_col01">
                    	    	<p><strong>  رقم المنافسة  </strong></p><p>NPT0036/23</p>
                    	    </div>
                    	    <div class="box_arbic_col02">
                            
                    	    	<p></p>
                    	    </div>

                    	    </div> 
                    	 	<p class="box_arbic_text_p">النتائج النهائية </p>
                    	 </div>

                       <div class="box_aric04">

                        
    <p> <strong> عنوان المنافسة </strong> </p> <p>منافسة تأمين محاليل ومستهلكات مقابل توريد الأجهزةReagent deal (طب نقل وبنوك الدم)</p>                  
                         </div> 
							     <div class="box_aric04 date-container">
							     <p><strong>  موعد استلام العروض :</strong>
						   <span>الثلاثاء 30-01-2024</span></p> 
                  
                        <p><strong> 
							تاريخ فتح المظاريف :</strong> 
						   <span>الأربعاء 31-01-2024</span></p> 
						   </div>
    
                      </a>
                                              
                         

                                         
                           
                              </div>



                        </div>
                        
                


                 
                </div>

                    
            </div>
        </div>
 
 
<style type="text/css">

	.mix{display: none;}
	.mix.open{display: inline-block;}
    
    .container{
  padding: 2% 2% 0;
  text-align: justify;
  font-size: 0.1px;
  background: #68b8c4;
  
  -webkit-backface-visibility: hidden;
}

.container:after{
  content: '';
  display: inline-block;
  width: 100%;
}

.container .mix,
.container .gap{
  display: inline-block;
  width: 49%;
}

.container .mix{
  text-align: left;
  background: #03899c;
  margin-bottom: 2%;
  display: none;
}

.container .mix.category-1{
  border-top: 2px solid limegreen;
}

.container .mix.category-2{
  border-top: 2px solid yellow;
}

.container .mix:after{
  content: attr(data-myorder);
  color: white;
  font-size: 16px;
  display: inline-block;
  vertical-align: top;
  padding: 4% 6%;
  font-weight: 700;
}

.container .mix:before{
  content: '';
  display: inline-block;
  padding-top: 60%;
}

@media all and (min-width: 420px){
  .container .mix,
  .container .gap{
    width: 32%;
  }
}

@media all and (min-width: 640px){
  .container .mix,
  .container .gap{
    width: 23.5%;
  }
}
</style>

			</div>
		<!-- /.tg-container-->
		</div>
		<!-- /#content-->
				</main><!-- /#main -->
		
			<footer id="colophon" class="site-footer tg-site-footer ">
		
		
		<div class="tg-site-footer-widgets">
			<div class="tg-container">
				
<div class="tg-footer-widget-container tg-footer-widget-col--four">
					<div class="tg-footer-widget-area footer-sidebar-1">
											<section id="text-1" class="widget widget_text"><h2 class="widget-title">الموقع</h2>			<div class="textwidget"><p>شارع سعيد السلمي، <i class="fa fa-map-marker"></i><br />
المدينة الرقمية<br />
الرياض 12251 &#8211; 2721<br />
المملكة العربية السعودية</p>
</div>
		</section><section id="text-16" class="widget widget_text">			<div class="textwidget"><p><a href="https://www.pif.gov.sa/ar/Pages/default.aspx#1"><img decoding="async" style="max-width: 200px;" src="https://www.nupco.com/wp-content/uploads/2021/04/LOGOP-removebg-preview.png" /></a></p>
</div>
		</section>									</div>
								<div class="tg-footer-widget-area footer-sidebar-2">
											<section id="text-4" class="widget widget_text"><h2 class="widget-title">أرقامنا</h2>			<div class="textwidget"><p><span>ت:</span> 920018184 966+<br />
<span>ت:</span> 114196543 966+</p>
</div>
		</section>									</div>
								<div class="tg-footer-widget-area footer-sidebar-3">
											<section id="text-2" class="widget widget_text"><h2 class="widget-title">تابعنا</h2>			<div class="textwidget"><div class="header-bar-social-icons">
<ul>
<li><a href="https://instagram.com/nupco.sa?igshid=YmMyMTA2M2Y=" target="_blank" rel="noopener"><i class="fa fa-instagram"></i><br />
</a></li>
<li></li>
<li><a href="https://twitter.com/nupco" target="_blank" rel="noopener"><i class="fa fa-twitter"></i><br />
</a></li>
<li></li>
<li><a href="https://www.linkedin.com/company/nupco-national-unified-procurement-medical-supplies-company-/" target="_blank" rel="noopener"><i class="fa fa-linkedin"></i><br />
</a></li>
<li></li>
</ul>
</div>
</div>
		</section><section id="text-14" class="widget widget_text"><h2 class="widget-title">حمل التطبيق</h2>			<div class="textwidget"><section id="text-2" class="widget widget_text">
<div class="textwidget">
<div class="header-bar-social-icons">
<a href="https://cutt.ly/VhVriYJ"><img decoding="async" src="https://www.nupco.com/wp-content/uploads/2021/01/nupco-mobile-app-08.png" style="max-width: 39%;margin-top:-12px;"></a><br />
<a href="https://apps.apple.com/sa/app/nupco/id1524469406"><img decoding="async" src="https://www.nupco.com/wp-content/uploads/2021/01/nupco-mobile-app-09.png" style="max-width: 39%;margin-top:-12px;"></a>
</div>
</section>
</div>
		</section>									</div>
								<div class="tg-footer-widget-area footer-sidebar-4">
											<section id="nav_menu-4" class="widget widget_nav_menu"><h2 class="widget-title">أخرى</h2><div class="menu-important-link-ar-container"><ul id="menu-important-link-ar" class="menu"><li id="menu-item-4044" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-4044"><a href="https://www.nupco.com/%d8%ae%d8%b7%d8%a9-%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a7%d8%aa-%d8%a7%d9%84%d8%b4%d8%b1%d8%a7%d8%a1-%d8%a7%d9%84%d9%85%d9%88%d8%ad%d8%af-%d9%84%d8%b9%d8%a7%d9%85-2020%d9%85/"><i class="fa fa-chevron-left" aria-hidden="true"></i> خطة المنافسات</a></li>
<li id="menu-item-4046" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-4046"><a href="https://www.nupco.com/%d8%a7%d9%84%d8%a5%d8%a8%d9%84%d8%a7%d8%ba-%d8%b9%d9%86-%d9%85%d8%ae%d8%a7%d9%84%d9%81%d8%a9/%d8%b3%d9%8a%d8%a7%d8%b3%d8%a9-%d8%a7%d9%84%d8%a7%d8%a8%d9%84%d8%a7%d8%ba-%d8%b9%d9%86-%d8%a7%d9%84%d9%85%d8%ae%d8%a7%d9%84%d9%81%d8%a7%d8%aa/"><i class="fa fa-chevron-left" aria-hidden="true"></i> سياسة الابلاغ عن المخالفات</a></li>
<li id="menu-item-4049" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-4049"><a href="https://www.nupco.com/%d8%a7%d9%84%d8%a5%d8%a8%d9%84%d8%a7%d8%ba-%d8%b9%d9%86-%d9%85%d8%ae%d8%a7%d9%84%d9%81%d8%a9/"><i class="fa fa-chevron-left" aria-hidden="true"></i> الإبلاغ عن مخالفة</a></li>
<li id="menu-item-4047" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-4047"><a href="https://www.nupco.com/%d8%a7%d8%b4%d8%aa%d8%b1%d9%83-%d9%81%d9%8a-%d9%86%d8%b4%d8%b1%d8%aa%d9%86%d8%a7-%d8%a7%d9%84%d8%a5%d8%ae%d8%a8%d8%a7%d8%b1%d9%8a%d8%a9/"><i class="fa fa-chevron-left" aria-hidden="true"></i> اشترك في نشرتنا الإخبارية</a></li>
<li id="menu-item-4048" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-4048"><a href="https://www.nupco.com/%d8%a7%d9%84%d8%aa%d8%b9%d9%84%d9%8a%d9%82%d8%a7%d8%aa-%d9%88%d8%a7%d9%84%d8%a5%d9%82%d8%aa%d8%b1%d8%a7%d8%ad%d8%a7%d8%aa/"><i class="fa fa-chevron-left" aria-hidden="true"></i> التعليقات والإقتراحات</a></li>
<li id="menu-item-16396" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-16396"><a href="https://www.nupco.com/marketplace/"><i class="fa fa-chevron-left" aria-hidden="true"></i>السوق الإلكتروني</a></li>
<li id="menu-item-15432" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-15432"><a href="https://www.nupco.com/%d8%b3%d8%ac%d9%84-%d8%a7%d9%87%d8%aa%d9%85%d8%a7%d9%85%d9%83/"><i class="fa fa-chevron-left" aria-hidden="true"></i>  سجل اهتمامك</a></li>
<li id="menu-item-26070" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-26070"><a href="https://www.nupco.com/%D8%A7%D9%84%D8%A7%D8%B4%D8%AA%D8%B1%D8%A7%D9%83-%D9%81%D9%8A-%D8%A7%D9%84%D9%86%D8%B4%D8%B1%D8%A9-%D8%A7%D9%84%D8%A8%D8%B1%D9%8A%D8%AF%D9%8A%D8%A9/"><i class="fa fa-chevron-left" aria-hidden="true"></i>اشترك في نشرتنا البريدية</a></li>
</ul></div></section>									</div>
				</div> <!-- /.tg-footer-widget-container -->
			</div><!-- /.tg-container-->
		</div><!-- /.tg-site-footer-widgets -->

		
		
		<div class="tg-site-footer-bar tg-site-footer-bar--center">
			<div class="tg-container tg-container--flex tg-container--flex-top">
				<div class="tg-site-footer-section-1">

					<section id="text-12" class="widget widget_text">			<div class="textwidget"><p>© 2023 نوبكو &#8211; الحقوق محفوظة.</p>
</div>
		</section>
				</div>
				<!-- /.tg-site-footer-section-1 -->

				<div class="tg-site-footer-section-2">

					
				</div>
				<!-- /.tg-site-footer-section-2 -->
			</div>
			<!-- /.tg-container-->
		</div>
		<!-- /.tg-site-footer-bar -->

		
			</footer><!-- #colophon -->
		
		</div><!-- #page -->
				<nav id="mobile-navigation" class="tg-mobile-navigation"
			>

			<div class="menu-main-arabic-container"><ul id="mobile-primary-menu" class="menu"><li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-home menu-item-15079"><a href="https://www.nupco.com/">الرئيسية</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-3700"><a href="#">لمحة عن نوبكو</a>
<ul class="sub-menu">
	<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-22358"><a href="https://www.nupco.com/%d8%a7%d9%84%d8%a7%d8%b3%d8%aa%d8%af%d8%a7%d9%85%d8%a9/">الاستدامة</a></li>
	<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-3766"><a href="https://www.nupco.com/%d9%84%d9%85%d8%ad%d8%a9-%d8%b9%d8%a7%d9%85%d8%a9/">لمحة عامة</a></li>
	<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-8143"><a href="https://www.nupco.com/members/">مجلس الادارة</a></li>
	<li class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-12574"><a href="https://www.nupco.com/category/%d8%a7%d9%84%d8%a3%d8%ae%d8%a8%d8%a7%d8%b1/">الأخبار</a></li>
	<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-9499"><a href="https://www.nupco.com/externalnewsletter/">نشرة نوبكو</a></li>
	<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-3767"><a target="_blank" rel="noopener" href="https://www.nupco.com/wp-content/uploads/2020/03/FAQ-v2.pdf">الأسئلة الشائعة</a></li>
	<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-7622"><a href="https://www.nupco.com/wp-content/uploads/2021/09/الدليل-الإرشادي-الموحد-لرحلة-الموردين.pdf">الدليل الإرشادي الموحد لرحلة المورد</a></li>
</ul>
</li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-4028"><a href="#">الخدمات الإلكترونية</a>
<ul class="sub-menu">
	<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-17945"><a href="https://inupco.nupco.com/suppliers/pre-registration">تسجيل الموردين</a></li>
	<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4030"><a target="_blank" rel="noopener" href="https://tenders.nupco.com/irj/portal">مزود الخدمة الذاتية</a></li>
	<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4031"><a target="_blank" rel="noopener" href="https://tenders.nupco.com/irj/portal">طلبات العملاء</a></li>
</ul>
</li>
<li class="menu-item menu-item-type-custom menu-item-object-custom current-menu-ancestor current-menu-parent menu-item-has-children menu-item-14427"><a href="#">المنافسات</a>
<ul class="sub-menu">
	<li class="menu-item menu-item-type-post_type menu-item-object-page current-menu-item page_item page-item-3715 current_page_item menu-item-3768"><a href="https://www.nupco.com/%d8%a7%d9%84%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a7%d8%aa/" aria-current="page">المنافسات المطروحة</a></li>
	<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-14633"><a href="https://www.nupco.com/%d8%a7%d9%84%d8%a3%d8%b3%d8%a6%d9%84%d8%a9-%d8%a7%d9%84%d8%b4%d8%a7%d8%a6%d8%b9%d8%a9-%d8%a7%d9%84%d8%ae%d8%a7%d8%b5%d8%a9-%d8%a8%d8%a7%d9%84%d9%85%d9%86%d8%a7%d9%81%d8%b3%d8%a7%d8%aa/">الأسئلة الشائعه الخاصة بالمنافسات</a></li>
</ul>
</li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-22433"><a href="https://www.nupco.com/%d8%a7%d9%84%d8%af%d9%84%d9%8a%d9%84-%d8%a7%d9%84%d9%85%d9%88%d8%ad%d8%af/">الدليل الموحد</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-25392"><a href="#">التوظيف و التدريب</a>
<ul class="sub-menu">
	<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4149"><a href="https://www.nupco.com/NupcoJobPortal/ar">التوظيف</a></li>
	<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-25391"><a href="https://www.nupco.com/%d8%a7%d9%84%d8%aa%d8%af%d8%b1%d9%8a%d8%a8/">التدريب</a></li>
</ul>
</li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-17595"><a href="https://inupco.nupco.com/home"><img src="https://www.nupco.com/wp-content/uploads/2023/07/box.png"></a></li>
<li class="menu-item tg-menu-item tg-menu-item-search"><a><i class="tg-icon tg-icon-search"></i></a><form role="search" method="get" class="search-form" action="https://www.nupco.com/">
				<label>
					<span class="screen-reader-text">البحث عن:</span>
					<input type="search" class="search-field" placeholder="بحث &hellip;" value="" name="s" />
				</label>
				<input type="submit" class="search-submit" value="بحث" />
			</form></li><!-- /.tg-header-search --></ul></div>
		</nav><!-- /#mobile-navigation-->
		
		<a href="#" id="tg-scroll-to-top" class="tg-scroll-to-top">
			<i class="tg-icon tg-icon-arrow-up"><span
						class="screen-reader-text">تمرير للأعلى</span></i>
		</a>

		<div class="tg-overlay-wrapper"></div>
		

<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script src="https://demo.tinywall.net/numscroller/numscroller-1.0.js"></script>

<script type="text/javascript" id="contact-form-7-js-extra">
/* <![CDATA[ */
var wpcf7 = {"apiSettings":{"root":"https:\/\/www.nupco.com\/wp-json\/contact-form-7\/v1","namespace":"contact-form-7\/v1"}};
/* ]]> */
</script>
<script type="text/javascript" src="https://www.nupco.com/wp-content/plugins/contact-form-7/includes/js/scripts.js?ver=5.1.6" id="contact-form-7-js"></script>
<script type="text/javascript" id="cf7msm-js-extra">
/* <![CDATA[ */
var cf7msm_posted_data = {"_wpcf7cf_hidden_group_fields":"[]","_wpcf7cf_hidden_groups":"[]","_wpcf7cf_visible_groups":"[]"};
/* ]]> */
</script>
<script type="text/javascript" src="https://www.nupco.com/wp-content/plugins/contact-form-7-multi-step-module/resources/cf7msm.min.js?ver=4.4" id="cf7msm-js"></script>
<script type="text/javascript" src="https://www.nupco.com/wp-content/plugins/date-time-picker-for-contact-form-7/assets/js/jquery.datetimepicker.full.min.js?ver=6.5.3" id="walcf7-datepicker-js-js"></script>
<script type="text/javascript" src="https://www.nupco.com/wp-content/plugins/date-time-picker-for-contact-form-7/assets/js/datetimepicker.js?ver=1.0.0" id="walcf7-datepicker-js"></script>
<script type="text/javascript" src="https://www.nupco.com/wp-content/themes/zakra/assets/js/navigation.min.js?ver=20151215" id="zakra-navigation-js"></script>
<script type="text/javascript" src="https://www.nupco.com/wp-content/themes/zakra/assets/js/skip-link-focus-fix.min.js?ver=20151215" id="zakra-skip-link-focus-fix-js"></script>
<script type="text/javascript" src="https://www.nupco.com/wp-content/themes/zakra/assets/js/zakra-custom.min.js?ver=6.5.3" id="zakra-custom-js"></script>
<script type="text/javascript" id="wpcf7cf-scripts-js-extra">
/* <![CDATA[ */
var wpcf7cf_global_settings = {"ajaxurl":"https:\/\/www.nupco.com\/wp-admin\/admin-ajax.php"};
/* ]]> */
</script>
<script type="text/javascript" src="https://www.nupco.com/wp-content/plugins/cf7-conditional-fields/js/scripts.js?ver=2.4.4" id="wpcf7cf-scripts-js"></script>

<script type="text/javascript">
$(document).ready(function(){
	$( ".search-form" ).append( "<i class='fa fa-times close-search' aria-hidden='true'></i>" );
   
});

$(document).ready(function(){
  $(".close-search").click(function(){
    $(".tg-menu-item-search").removeClass("show-search");
  });
});
</script>

<script>
  window.fcWidget.init({
    token: "6732b167-01ba-4679-8e73-50349eb770a5",
    host: "https://wchat.freshchat.com",
      locale: "ar",
      config: {
          headerProperty: {
              direction: 'rtl'
          },
          content: {
              headers: {
                  chat: 'اختر نوع المحادثة',
                  chat_help: 'فريق نوبكو يسعد بخدمتك',
                  faq: 'معلومات تهمك',
                  faq_help: 'اختر من القائمة في الأسفل',
                  faq_not_available: 'راجع الأسئلة الشائعة في الموقع',
                  faq_search_not_available: 'لايوجد سؤال مماثل {{query}}',
                  faq_useful: 'هل تمت الإجابة على سؤالك؟',
                  faq_thankyou: 'شكراً لك',
                  faq_message_us: 'راسلنا بخصوص الأسئلة الشائعة',
                  push_notification: 'اريد استلام الإشعارات',
                  csat_question: 'هل أنت راضي على الخدمة؟',
                  csat_yes_question: 'مستوى رضاك من الخدمة',
                  csat_no_question: 'رضاك يهمنا ستقوم الإدارة بمراجعة المحادثة',
                  csat_thankyou: 'شكراً لتجاوبك',
                  csat_rate_here: 'قيم الخدمة هنا',
                  channel_response: {
                      offline: 'حالياً لسنا موجودين',
                      online: {
                          minutes: {
                              one: "سيتم الرد عليك خلال لحظات",
                              more: "سيتم الرد عليك خلال {{time}} دقائق"
                          },
                          hours: {
                              one: "سيتم الرد عليك خلال",
                              more: "سيتم الرد عليك خلال {{time}} ساعة",

                          }
                      }
                  }
              },
              placeholders: {
                  search_field: 'ابحث هنا',
                  reply_field: 'اكتب هنا',
                  csat_reply: 'يرجى كتابة ملاحظاتك'
              },
              actions: {
                  csat_yes: 'راضي',
                  csat_no: 'غير راضي',
                  push_notify_yes: 'فعّل الاشعارات',
                  push_notify_no: 'ايقاف الإشعارات',
                  tab_faq: 'معلومات تهمك',
                  tab_chat: 'المحادثة الفورية',
                  csat_submit: 'ارسال'
              },
          },
          cssNames: {
              widget: 'fc_frame',
              open: 'fc_open',
              expanded: 'fc_expanded'
          },
      },
  });
        </script>

        <script>
        (function (i, s, o, g, r, a, m) {
            i['GoogleAnalyticsObject'] = r; i[r] = i[r] || function () {
                (i[r].q = i[r].q || []).push(arguments)
            }, i[r].l = 1 * new Date(); a = s.createElement(o),
                m = s.getElementsByTagName(o)[0]; a.async = 1; a.src = g; m.parentNode.insertBefore(a, m)
        })(window, document, 'script', 'https://www.google-analytics.com/analytics.js', 'ga'); 
        ga('create', 'UA-97638893-1', 'auto');
        ga('send', 'pageview'); 
    </script>
	<!-- Google tag (gtag.js) -->
	<script async src="https://www.googletagmanager.com/gtag/js?id=G-1TLN228RCG"></script>
	<script>
		window.dataLayer = window.dataLayer || [];
		function gtag(){dataLayer.push(arguments);}
		gtag('js', new Date());

		gtag('config', 'G-1TLN228RCG');
	</script>

</body>
</html>
 <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
<script type="text/javascript" src="https://cdn.jsdelivr.net/jquery.mixitup/latest/jquery.mixitup.min.js"></script>
<script type="text/javascript">
    //Filters Section / Mixitup
    jQuery(function(){
  jQuery('#Container').mixItUp();
});
</script>

"""
matches = re.findall(pattern, text)

# Function to find the specific PDF link in the page content
def find_specific_pdf_link(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            # Search for the string 'target="_blank"> النتائج النهائية'
            search_string = 'target="_blank"> النتائج النهائية'
            if search_string in response.text:
                # Extract the <a> tag containing the search_string
                link = soup.find('a', text='النتائج النهائية', target='_blank')
                if link and link['href'].endswith('.pdf'):
                    print('final',link['href'])
                    return link['href']
        return None
    except Exception as e:
        print(f"Error accessing {url}: {e}")
        return None

# Create a DataFrame from the matches
df = pd.DataFrame(matches, columns=['URLs'])

# Find the specific PDF links for each URL and store in the DataFrame
df['PDF Links'] = df['URLs'].apply(find_specific_pdf_link)

# Save to Excel
df.to_excel('nupco_links_with_pdfs1.xlsx', index=False)

print(f"Processed {len(matches)} URLs and saved to 'nupco_links_with_pdfs1.xlsx'")