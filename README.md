Steps Performed
Feature Separation: Isolated true measurements (Age, Fare, SibSp, Parch) from structural tags (PassengerId, Survived, Pclass) to avoid corrupting categories.
Missing Values: Replaced missing numerical numbers with the column median and text entries with the column mode.
Encoding: Encoded text features into clean binary columns.
Outlier Filtering: Handled outliers on true measurements using the IQR method.
Scaling: Standardized numerical columns using StandardScaler to bring them to a common scale.
