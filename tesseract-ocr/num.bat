echo Run Tesseract for Training.. 

tesseract.exe bchuan.test.exp0.tif bchuan.test.exp0 nobatch box.train 

 

echo Compute the Character Set.. 

unicharset_extractor.exe bchuan.test.exp0.box 

mftraining -F font_properties -U unicharset -O num.unicharset bchuan.test.exp0.tr 

 

echo Clustering.. 

cntraining.exe bchuan.test.exp0.tr 

 

echo Rename Files.. 

rename normproto num.normproto 

rename inttemp num.inttemp 

rename pffmtable num.pffmtable 

rename shapetable num.shapetable  

 

echo Create Tessdata.. 

combine_tessdata.exe num.