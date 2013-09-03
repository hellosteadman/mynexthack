$(document).ready(
	function() {
		$('img.loading').on('load',
			function() {
				$(this).removeClass('loading');
			}
		);
		
		$('textarea.code').bind('click',
			function() {
				$(this).select();
			}
		);
		
		$('a.tweet-window').bind('click',
			function(e) {
				var width = 455;
				var height = 257;
				
				e.preventDefault();
				
				window.open(
					$(this).attr('href'),
					'tweet-window',
					'location=no,scrollbars=no,resizable=no,toolbar=no,menubar=no,width=' + width + ',height=' + height
				);
			}
		);
	}
);