import pandas as pd
train_df = pd.read_csv('./train_preprocessed.csv')
test_df = pd.read_csv('./test_preprocessed.csv')
correlation_df = train_df.corr()
print(correlation_df)
print("correlation between ‘survived’ and ‘sex’ column ", train_df['Sex'].corr(train_df['Survived']))