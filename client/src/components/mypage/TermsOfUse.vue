<template>
  <div>

    <v-dialog
      v-model="showTermsOfUse"
      fullscreen
    >
      <v-card>
        <h2 class="head d-flex justify-center" style="padding: 12px; background-color: white;"> TermsOfUse </h2>
          <v-btn
            icon
            class="close-dialog"
            @click="hideDialog"
          >
            <v-icon>mdi-close</v-icon>
        </v-btn>
        <h5 v-for="(term,idx) in terms" :key="idx">{{ term }}</h5>

      </v-card>

    </v-dialog>
  </div>
</template>

<script>
export default {
  props: ['showTermsOfUse'],
  data: () => ({
    terms: ['1. Purpose', 'The purpose of these terms and conditions is to stipulate the rights and obligations of the "company" and users(hereinafter referred to as the "Customers"), responsibilities, and other matters in using the learning services(hereinafter referred to as the "Service") provided by Team.ㅇ1ㄱ4(hereinafter referred to as the "Company")',
    '2. Service contents', 'This service provides free learning based on Korean cultural contents (movies, dramas, music, etc.). The service was created for a non-commercial purpose. Also, there is no way to take advantage of any interest rate within the service. Accordingly, the company is not responsible for any financial damages arising after using the service.',
    '3. Membership registration and information change', '3-1. This service can be used after completing the membership registration process, and if the information entered at the time of membership registration is changed, the customer must directly modify it within the app.', '3-2. The company is not responsible for any disadvantages caused by the customer not notifying the company of the member information changes in Paragraph 3-1.',
    '4. Service configuration', '4-1. The contents of this service are largely composed of learning, testing, and achievements.','4-2. In the learning page, you can study by category (movie, drama, music).','4-3. In the test page, you can take the test based on what you have learned so far.',"4-4. In the achievements window, you can check the badges (only within the app) obtained based on the customer's activity.",
    '5. Intellectual property', 'This service was created based on Korean cultural contents (movies, dramas, music, etc.). Accordingly, you can check the contents of the rights at any time within the app, and if a problem occurs in the future, you can stop the service at any time. In addition, if a customer uses the service commercially in any form, all liability lies with the customer.',
    '6. Content usage restrictions', '6-1. All content cannot be issued, redistributed, redistributed, or resold (distributed, transferred, loaned, rented, or rented).', '6-2. All contents cannot be used for the following purposes. ① Uses that hinder social breezes, such as pornography and adult advertisements, entertainment businesses, money-making businesses, and other customs businesses ② Other illegal use.', '6-3. All content is non-commercial and is provided for simple learning. Therefore, it is forbidden to reprocess it (secondary creation, etc.). All responsibility for this lies with the customer.',
    '7. Restrictions on or termination of service use', '7-1. The service may be discontinued or modified at any time.',
    "8. Company's obligations", '8-1. The company shall do its best to provide the service continuously and stably in accordance with these terms and conditions.','8-2. The Company shall promptly handle customer complaints related to the service, and if immediate processing is difficult, the Company shall notify the customer of the reason and processing schedule via e-mail.','8-3. All customer information provided to the company is encrypted and will not be reused for any reason.','8-4. If the service is interrupted, it must be notified in advance, and all customer information will be destroyed.',
    "9. Customer's obligations", "9-1. The customer must comply with the matters notified by the company, such as related laws and regulations, the provisions of these terms and conditions, usage guidelines and precautions, and must not engage in any other acts that interfere with the company's business.", '9-2. Customers shall not engage in any of the following actions in relation to the use of the service.',"1) Misuse of another member's ID", '2) Acts for the purpose of criminal activity or related to other criminal activities', '3) Acts that infringe on the rights of others, such as intellectual property rights', '4) Collecting or storing personal information about others', '5) Hacking or spreading computer viruses', '6) Continuously transmitting certain contents such as advertising information against the will of others', '7) Any action that interferes with or is likely to interfere with the stable operation of the service', '8) Acts that violate related laws', '9) Other actions that the company deems inappropriate for service operation ',
    '10. Notice to Customers', 'If the company notifies customers, it can be done by online service, email, SMS, etc. unless otherwise specified in these terms and conditions.',
    '11. Liability for damages', 'When either the company or the customer neglects or delays the performance of the obligations specified in these terms and conditions of service, the party who caused the act shall be fully responsible for such non-performance, and the other party shall compensate for any damages resulting therefrom. Any appropriate action required must be taken.',
    '12. Interpretation of the contract','Any objection to the interpretation of these Terms of Service or matters not specified in the Terms of Use shall be subject to mutual agreement between the Company and the customer.',
    '13. Obligation to protect personal information',"The company strives to protect the personal information of customers in accordance with relevant laws such as the “Information and Communication Network Act”. Regarding the protection and use of personal information, the relevant laws and the company's privacy policy apply.",
    '14. Compensation for damages',"If damage occurs to the customer due to the service provided by the company, the company shall be liable for damages within the scope of normal damage only if the damage is caused by the company's intention or gross negligence.",
    '15. Escape clause', '15-1. The company is not responsible for the provision of the service if it is unable to provide the service due to natural disasters, war, or other equivalent force majeure.', '15-2.The company shall not be held liable for damages caused by the telecommunication service provider suspending or not providing telecommunication services normally.', '15-3. The company is not responsible for any damages caused by unavoidable reasons such as maintenance, replacement, regular inspection, and construction of service facilities.', '15-4. The company is not responsible for any obstacles or damages in using the service due to reasons attributable to the customer.', "15-5. The Company shall not be held liable for any damages caused by a customer's computer error, or in the event of damages caused by incorrectly entering personal information or e-mail address by the customer.", '15-6. The company is not responsible for the learning outcomes customers expect from using the service.', '15-7. The company is not responsible for any damages caused by the data obtained by the customer while using the service. In addition, the company is not responsible for compensating for mental damage caused by other people while the customer uses the service.', '15-8. The company is not responsible for the reliability and accuracy of various information, data, and facts posted by customers on the service.', '15-9. The company is not obligated to intervene in disputes arising between customers and between customers and third parties through service, and is not responsible for any damages resulting from this.',
    '16. Tribunal rights and laws of compliance', "Matters not specified in these terms and conditions are subject to related laws and business practices such as the Telecommunications Business Act. When a lawsuit is filed for a dispute with a customer arising from the use of the service, the court having jurisdiction over the location of the company's headquarters shall be the competent court.",
    '※ Addendum', '(Enforcement Date) These terms and conditions will be applied from April 01, 2021.'

    ]
  }),
  methods: {
    hideDialog () {
      this.$emit('hideTutorial')
    }
  }
  
}
</script>

<style>

h5 {
  margin-left: 2%;
  margin-top: 2%;
  margin-right: 2%;
}


</style>