/**
 * Automatic Figure Numbering
 * Adds "Fig. X: " prefix to all figcaption elements
 * 
 * Configuration:
 * - SHOW_EMPTY_CAPTIONS: if true, shows "Fig. X" for empty captions
 *                        if false, hides empty figcaptions entirely
 */

(function() {
    'use strict';
    
    // Configuration
    var CONFIG = {
        SHOW_EMPTY_CAPTIONS: false  // Set to false to hide empty figcaptions
    };
    
    function numberFigures() {
        // Get all figcaption elements in the document
        var figcaptions = document.querySelectorAll('figcaption');
        
        // Counter for figure numbers
        var figureNumber = 1;
        
        // Iterate through each figcaption
        figcaptions.forEach(function(caption) {
            // Check if it already has a figure number to avoid double-numbering
            if (!caption.textContent.trim().startsWith('Fig')) {
                // Get the current text content
                var currentText = caption.textContent.trim();
                
                // Handle empty captions
                if (currentText === '') {
                    if (CONFIG.SHOW_EMPTY_CAPTIONS) {
                        // Show just "Fig. X" without colon
                        caption.textContent = 'Figure ' + figureNumber;
                    } else {
                        // Hide the empty caption
                        caption.style.display = 'none';
                        return; // Skip incrementing the figure number
                    }
                } else {
                    // Add the figure number prefix with colon
                    caption.textContent = 'Figure ' + figureNumber + ': ' + currentText;
                }
                
                // Increment the counter
                figureNumber++;
            }
        });
    }
    
    // Run when DOM is fully loaded
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', numberFigures);
    } else {
        // DOMContentLoaded has already fired
        numberFigures();
    }
})();
