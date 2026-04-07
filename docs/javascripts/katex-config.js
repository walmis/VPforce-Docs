function renderKaTeXMath() {
  if (typeof renderMathInElement !== 'function') {
    return;
  }

  // Arithmatex already wraps expressions in span/div.arithmatex, so render only those nodes.
  document.querySelectorAll('.arithmatex').forEach(function(element) {
    if (element.dataset.katexRendered === 'true') {
      return;
    }

    renderMathInElement(element, {
      delimiters: [
        {left: '$$', right: '$$', display: true},
        {left: '$', right: '$', display: false},
        {left: '\\(', right: '\\)', display: false},
        {left: '\\[', right: '\\]', display: true}
      ],
      throwOnError: false
    });

    element.dataset.katexRendered = 'true';
  });
}

document.addEventListener('DOMContentLoaded', renderKaTeXMath);
document.addEventListener('mkdocs:document$', renderKaTeXMath);
