#!/bin/bash
# Download nltk data
python -c "import nltk; nltk.download('punkt');"
# Download PPDB
mkdir resources; cd resources;
wget https://github.com/ma-sultan/monolingual-word-aligner/raw/master/Resources/ppdb-1.0-xxxl-lexical.extended.synonyms.uniquepairs
cd -
# Download UCCA semantic parsing model
mkdir resources/ucca; cd resources/ucca;
curl -LO https://github.com/huji-nlp/tupa/releases/download/v1.3.6/ucca-bilstm-1.3.6.tar.gz
tar xvzf ucca-bilstm-1.3.6.tar.gz
cd -
