// INLINE CODE PLUGIN
(function() {
	(function($) {
		// The plugin named "code"
		return $.widget('IKS.code', {
			options: {
				uuid: '',
				editable: null
			},
			populateToolbar: function(toolbar) {
				var button, widget;

				widget = this;

				// Helper method to get currently selected <code> tag
				// e.g. did we select a text which already wrapped in <code>?
				getEnclosingCode = function() {
					var node;
					node = widget.options.editable.getSelection().commonAncestorContainer;
					return $(node).parents('code').get(0);
				};

				// Creates the editor button
				button = $('<span></span>');
				button.hallobutton({
					uuid: this.options.uuid,
					editable: this.options.editable,
					label: 'Inline Code',
					icon: 'icon-code',
					command: null,
					// Method to check if button is active
					// e.g. when cursor is inside a <code> tag
					queryState: function(event) {
						return button.hallobutton('checked', !!getEnclosingCode());
					}
				});

				toolbar.append(button);

				// Defines what will happen when button clicked
				button.on('click', function(event) {
					var enclosingCode = getEnclosingCode();
					var lastSelection = widget.options.editable.getSelection();

					// Pressing the button inside a code tag
					// will delete the code tag.
					if (enclosingCode) {
						$(enclosingCode).replaceWith(enclosingCode.innerHTML);
						button.hallobutton('checked', false);
						return widget.options.editable.element.trigger('change');
					}

					// Pressing the button with a selection outside a code tag
					// will wrap the selection in a <code> tag
					if (!lastSelection.collapsed && !enclosingCode) {
						var elem = "<code>" + lastSelection + "</code> ";
						lastSelection.deleteContents();
						lastSelection.insertNode(lastSelection.createContextualFragment(elem));
						return widget.options.editable.element.trigger('change');
					}

					// Pressing the button with no selection outside a code tag
					// is tricky so we don't handle it :-p
					if (lastSelection.collapsed && !enclosingCode) {
						alert('Select text to wrap in a code tag');
					}
				});
			}
		});
	})(jQuery);
}).call(this);
