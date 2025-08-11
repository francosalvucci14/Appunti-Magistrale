const { Plugin } = require('obsidian');
const { Prec } = require('@codemirror/state');
const { EditorView } = require('@codemirror/view');

module.exports = class AutoBracesPlugin extends Plugin {
  onload() {
    const domHandler = EditorView.domEventHandlers({
      keyup: (event, view) => {
        if (event.ctrlKey || event.metaKey || event.altKey) return false;
        if (event.isComposing) return false;

        const key = event.key;
        if (key !== '_' && key !== '^') return false;

        const pos = view.state.selection.main.head;
        const docStr = view.state.doc.toString();

        if (!this._isInMath(docStr, pos)) return false;

        // Controlla se subito prima del cursore c'è proprio il carattere appena digitato
        const before = view.state.doc.sliceString(pos - 1, pos);
        if (before !== key) return false;

        // Sostituisci il carattere con parentesi
        view.dispatch({
          changes: {
            from: pos - 1,
            to: pos,
            insert: `${key}{}`
          },
          selection: { anchor: pos + 1 } // cursore dentro le {}
        });

        return true;
      }
    });

    this.registerEditorExtension(Prec.high(domHandler));
    console.log('AutoBraces (post-insert) loaded');
  }

  _isInMath(doc, pos) {
    // euristica: controlla se numero di $ o $$ prima del cursore è dispari
    let doubleDollar = 0, singleDollar = 0;
    for (let i = 0; i < pos; i++) {
      if (doc[i] === '$') {
        if (i + 1 < doc.length && doc[i + 1] === '$') {
          doubleDollar++;
          i++;
        } else {
          singleDollar++;
        }
      }
    }
    return (doubleDollar % 2 === 1) || (singleDollar % 2 === 1);
  }

  onunload() {
    console.log('AutoBraces unloaded');
  }
};
