import streamlit as st

st.markdown(
    """
    <style>
    body {
        direction: rtl;
        text-align: right;
    }
    .css-1d391kg {
        text-align: right;
    }
    .css-10trblm {
        direction: rtl;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Render the chart in Streamlit using streamlit.components.v1.html
st.title("وش ينتظرك بعد التخرج؟")
st.html('''
<p>الهاجس الي ما فيه طالب الا وقد حس فيه, هو مستقبل ما بعد التخرج هل بيكون هذا الطالب موظف؟ هل ايجاد  الوظائف صعب؟ اسئلة مثل هذي تطري على البال كثير, لكن وش جوابها؟
شاب اسمه أحمد حديث تخرج من مدينة الدمام ويملك هذي المخاوف خلال بحثه عن وظيفة</p>
''')


st.image(r"img1.png", use_column_width=True)  # Adjust the path to your image file
st.html('''
<p> لاحظ احمد ان أكثر العروض الوظيفية تكون في منطقة الرياض, وهذا يرجع لأنها مدينة كبيرة وأيضا لأنها عاصمة المملكة, كذلك مكة المكرمة فيها فرص وظيفية كثيرة الي تمثل 25% من اجمالي الوظائف المعروضة, المنطقة الشرقية أيضا فيها فرص وظيفية ممتازة </p>
''')
st.image(r"img2.png", use_column_width=True)  # Adjust the path to your image file

st.html('''
<p>احمد فكر انه ممكن تكون هذي الفرص الوظيفية متحيزة الى جنس معين, بعد البحث لاحظ ان اغلب الوظائف المعروضة ما تحدد جنس على انه شرط للوظيفة, فيه نسبة من الوظائف تشترط ان يكون المتقدم ذكر او انثى لكن نسبتهم متقاربة</p>
''')
st.image(r"img3.png", use_column_width=True)  # Adjust the path to your image file
st.html('''
<p>لاحظ أحمد ان الرواتب المعروضة تتراوح ما بين 3 آلاف ريال سعودي وممكن تصل الى 13 ألف ريال سعودي, الا انه لاحظ ان اغلبية الوظائف تتراوح رواتبها ما بين 4 الاف الى 5 الاف</p>
''')
st.image(r"img4.png", use_column_width=True)  # Adjust the path to your image file
st.html('''
<p>الشي الي طمن أحمد انه أغلب الوظائف المعروضة كانت تستهدف حديثين التخرج وكانت تشكل 57% من الوظائف المعروضة, فرح أحمد بهذي النتيجة وتوكل على الله وبدأ يقدم وهو متطمن</p>
''')
