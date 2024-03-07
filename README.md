# BE Project Group 36 : Veritas Sponsored
## Identify Customer Name Varitaions using ML Techniques

### Steps To Complete: 
1) Data Collection and study of dataset
2) Data Preprocessing
3) Training dataset creation
4) SVM model training (currently in progress)
5) Try Random Forest
6) increase the accuracy of ML models used (SVM & Rondom Forest)
7) Building Frontend and Backend (Web Application)


### Last Week's College Review3: Teachers Feedback
1. Fuzzy Functions: instead of using in-built library define your our class and implement entire logic and use it
2. try to add more attributes like 'Cosine similarity', 'Jaccard coefficient' etc to increase the accuracy
3. draw own implemented class diagram 


## work in progress in coding 
## Steps to process the uploaded input file and daal file
1. firstly read input file and daal file, store them in 2 different dataframes.
2. Iterate on 'input_file_df' and for each record from input file, find top 3 matching records from "daal_file_df" using fuzzyMatchPercentage. (threshold 80% above)
3. While finding top 3 matching records :
    3.1. filter entire 'daal_file_df' dataframe accoring to common country names.
    3.2. if out of 3 top matching records, if at any point found 100% fuzzMatched , skip processing of remaining daal file (time will be reduced)
4. create 'new_df' with 2 columns as 'company name' (from input file) and 'similar company name' (from daal file), after done with step 2 and 3.
5. now calculate other 7 attributes i.e. values of simple ratio, partial ratio, token set ratio, ngram, charact_matching_percentage etc. and add these columns to 'new_df'
6. pass this 'new_df' to ML model for prediction of 'output' column as 0/1. And store only records with output = 1 (same) into final_df passed to flask application.

### processing time study:
1. for 10 input records => 3.3 sec
2. for 50 input records => 19.7 sec
3. for 100 input records => 44.3 sec

### Doubts:
1. 'output' target column => not giving specific correct prediction yet. (1->matched) (0->notMatched) manually checked but showing contradiction