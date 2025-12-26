from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

DATA_PATH='S:RestaurantData.csv'
df=pd.read_csv(DATA_PATH)

@app.route('/',methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/recommend',methods=['POST'])
def recommend():
    try:
        cuisine=request.form.get('cuisine')
        price_range=int(request.form.get('price_range'))
        online_delivery=request.form.get('online_delivery')

        filtered=df.copy()

        filtered=filtered[
            filtered['Cuisines'].str.contains(cuisine, case=False, na=False)
        ]

        filtered=filtered[filtered['Price range'] == price_range]

        filtered=filtered[
            filtered['Has Online delivery'] == online_delivery
        ]

        filtered=filtered.sort_values(
            by='Aggregate rating',ascending=False
        )

        recommendations=filtered.head(5)[
            [
                'Restaurant Name',
                'Cuisines',
                'Average Cost for two',
                'Aggregate rating',
            ]
        ].to_dict('records')

        if len(recommendations)==0:
            return render_template(
                'home.html',
                error='No restaurant found for given preference.',
            )

        return render_template(
            'home.html',recommendations=recommendations
        )

    except Exception as e:
        return render_template(
            'home.html',error=str(e))

if __name__=='__main__':
    app.run(debug=True)


