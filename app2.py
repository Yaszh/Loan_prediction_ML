import streamlit as st 
import numpy as np
import pickle 

loaded_model = pickle.load(open('trained_model.pkl','rb'))

# creating a function for prediction

def loan_prediction(input_data):
    input_np =np.asarray(input_data) 

    input_reshape = input_np.reshape(1,-1)

    prediction = loaded_model.predict(input_reshape)
    print(prediction)

    if(prediction[0]==0):
        return 'Your Loan is Passed'
    else:
        return 'Your Loan is Rejected'



def main():
    st.title('Loan Prediction Web App') 
    st.write('This app helps you to know whether an Applicant is eligible to get a Loan from the bank or not.')
        
    st.write("For giving input in the given parameters consider the following notations")
    st.write('Male-->0, Female-->1')
    st.write('Yes-->0, No-->1')
    st.write('Rural-->0, Urban-->1,SemiUrban-->2')
    
    
    st.title('Enter the details:')
    Gender = st.text_input('Gender ')
    Married = st.text_input('Martial Status(Married or not)')
    Dependents    = st.text_input('No. of Dependents')
    Education = st.text_input(' Education, (Graduate or not)')
    Self_Employed= st.text_input('Self Employed?(Yes or No)')
    ApplicantIncome= st.text_input('Application Income')
    CoapplicantIncome = st.text_input('Coapplicant Income')
    LoanAmount = st.text_input('LoanAmount')
    Loan_Amount_Term= st.text_input('Loan Amount Term')
    Credit_History = st.text_input('Credit History')
    Property_Area= st.text_input('Property Area')
    
        

    loan = ''

        # create a button or predict

    if st.button("Your Loan Status"):
        loan = loan_prediction([Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area])

    st.success(loan)


if __name__=='__main__':
    main()