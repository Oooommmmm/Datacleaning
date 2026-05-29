Steps Performed:<br>
<ul>
<li>Feature Separation: Isolated true measurements (Age, Fare, SibSp, Parch) from structural tags (PassengerId, Survived, Pclass) to avoid corrupting categories.<br>
<li>Missing Values: Replaced missing numerical numbers with the column median and text entries with the column mode.<br>
<li>Encoding: Encoded text features into clean binary columns.<br>
<li>Outlier Filtering: Handled outliers on true measurements using the IQR method.<br>
<li>Scaling: Standardized numerical columns using StandardScaler to bring them to a common scale.<br>
</ul>
