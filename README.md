<p align="center">
    <img src=".github/logo.svg?sanitize=true" />
</p>

<p align="center"> 
    <img src="https://img.shields.io/github/license/tquangsdh20/data-mining"> <img src = "https://img.shields.io/github/issues/tquangsdh20/data-mining"> <img src="https://img.shields.io/github/languages/count/tquangsdh20/data-mining"> <img src="https://img.shields.io/badge/R-v4.0.5-orange"> <img src = "https://img.shields.io/pypi/pyversions/memrise"> <img src="https://img.shields.io/github/last-commit/tquangsdh20/data-mining">
</p>

## Data-Mining Mini Project

### Data Collection

<div align="justify">
All data is collected from <a href="https://hopamchuan.com">HopAmChuan</a> store in the <i>Data Warehouse</i> with the purpose is based on the playlist of the user to analyze and recommend similar songs that the user might like them. The Data Warehouse has the <i>Entity Relationship Diagram</i> as the following.  </div>

### Entity Relationship Diagram

<p align="center">
<img src=".github/ERD.svg?sanitize=true" height="500" width="800">
</p>

### Pivot Table

<table class="dataframe">
<caption>Aggregates the individual items for get the specific table relative to the specific user</caption>
<thead>
	<tr><th>SongID</th><th scope=col>bollero</th><th scope=col>ballad</th><th scope=col>blue</th><th scope=col>bossanova</th><th scope=col>rock</th><th scope=col>chachacha</th><th scope=col>fox</th><th scope=col>rhumba</th><th scope=col>boston</th><th scope=col>disco</th><th scope=col>pop</th><th scope=col>slow</th><th scope=col>slowrock</th><th scope=col>tango</th><th scope=col>valse</th></tr>
</thead>
<tbody>
	<tr><th scope=row>1911</th><td>24</td><td>10</td><td>2</td><td>2</td><td>2</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td> 0</td><td> 0</td><td>0</td><td> 0</td></tr>
	<tr><th scope=row>7073</th><td> 1</td><td> 5</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td> 0</td><td> 4</td><td>0</td><td> 0</td></tr>
	<tr><th scope=row>769</th><td> 2</td><td>32</td><td>2</td><td>0</td><td>5</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td> 9</td><td>57</td><td>0</td><td> 0</td></tr>
	<tr><th scope=row>4618</th><td> 1</td><td>25</td><td>8</td><td>1</td><td>3</td><td>2</td><td>2</td><td>3</td><td>0</td><td>0</td><td>4</td><td>74</td><td>11</td><td>6</td><td>14</td></tr>
	<tr><th scope=row>9460</th><td>39</td><td>10</td><td>1</td><td>0</td><td>0</td><td>3</td><td>0</td><td>1</td><td>3</td><td>1</td><td>0</td><td> 2</td><td>10</td><td>0</td><td> 0</td></tr>
	<tr><th scope=row>3368</th><td>73</td><td>23</td><td>3</td><td>0</td><td>0</td><td>2</td><td>1</td><td>4</td><td>3</td><td>7</td><td>1</td><td>13</td><td> 2</td><td>1</td><td> 0</td></tr>
</tbody>
</table>
