(function() {
	'use strict';

	// https://remysharp.com/2010/07/21/throttling-function-calls
	function throttle(fn, threshhold, scope) {
		threshhold || (threshhold = 250);
		var last,
		deferTimer;
		return function () {
			var context = scope || this;

			var now = +new Date,
			args = arguments;
			if (last && now < last + threshhold) {
				// hold on to it
				clearTimeout(deferTimer);
				deferTimer = setTimeout(function () {
					last = now;
					fn.apply(context, args);
				}, threshhold);
			} else {
				last = now;
				fn.apply(context, args);
			}
		};
	}

	var setStickyFooterHeight = throttle(function () {
		var footerElm = document.getElementsByClassName('js-site-footer');
		if (footerElm.length === 0) {
			return;
		}

		var footerHeight = footerElm[0].offsetHeight;
		document.body.style.marginBottom = footerHeight + 'px';
	}, 50);

	document.addEventListener('DOMContentLoaded', setStickyFooterHeight);
	window.addEventListener('resize', setStickyFooterHeight);


	// Animate the Technology pane items when the waypoint is scrolled to
	// (or already in view).
	(function () {
		var elm = document.getElementsByClassName('js-technology-pane-waypoint');
		if (elm.length === 0) {
			return;
		}

		elm[0].className += ' animation-fade-in--pre';

		var waypoint = new Waypoint({
			element: elm[0],
			offset: 'bottom-in-view',
			handler: function() {
				elm[0].className = elm[0].className.replace(
					'animation-fade-in--pre',
					'animation-fade-in--start'
				)
			}
		});

	})();
})();
