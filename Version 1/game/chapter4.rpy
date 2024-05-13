# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The game starts here.

#sub chapter 1 

#character 
define ManuelQuezon = Character("Manuel Quezon", color="#ff8c00", voice_tag="ManuelQuezon")
define Speaker= Character("Speaker", color="#ffbbbb", voice_tag="Speaker")
define person1 = Character("Person 1", color="#fcbf31", voice_tag="person1")
define person2 = Character("Person 2", color="#ffa9a9", voice_tag="person2")
define person3 = Character("Person 3", color="#d2a2fc", voice_tag="person3")
define person4 = Character("Person 4", color="#a7ffc5", voice_tag="person4")

#sub chapter 2 Character
define CIAExecutive = Character("CIA Executive", color="#777875", voice_tag="CIAExecutive")
#scene1


label chapter_4:
    show bg black

    call slowTextfade("The Philippines Under the United States")

    call subChapter1

    return


label subChapter1:
    #(Filipino Grievances Against Governor-General Wood)
    #SCENE1

    show bg black
    call slowTextfade("Filipino Grievances Against Governor-General Wood")
    play music "/music/bg_ph_street.mp3" fadein 0.5 volume 0.2

    scene bg street with fade

    show mc thinking2 at left

    "..." " [mc] gets teleported to a street in Manila noticing the different scenery and ambiance"
    "..." " [mc] sees 5 people storming out of a building one of which [mc] remembers to be Manuel Quezon"
    "..." "shortly after storming out of the building Manuel Quezon separates from the group"
    
    menu:
        "Manuel Quezon separated from the group, I should..."

        "Follow Manuel Quezon":
            "[mc] (Inner thoughts)" "He doesn't seem to be particularly important right now"
            jump textEvent6
        "Ignore him and follow the other 4":
            jump textEvent6

    
label textEvent6:
    "..." "[mc] decides to follow the other 4 people who seem to be walking towards an alley-way."
    play sound "audio/Footstep concrete.mp3" volume 0.2
    "..." "Along the way the [mc] listens in to the 4 people gossiping."

    mc "(Looking around) Teka, nasaan ako? Ibang-iba to sa lugar kung saan ako nung una. (Spots Manuel Quezon and the group) Teka, hindi ba si Manuel Quezon yan? Dapat ko silang sundan"
    hide mc

    show manuel default
    ManuelQuezon "(Storming out of the building) Hindi ako makapaniwala dito! Isa na namang desisyon na pabor sa mga Amerikano kaysa sa mga kapwa pilipino"
   
    hide manuel

    show crowd
    show mc realization at right

    mc "(Following the group) Mukhang galit sila sa isang bagay. Malapitan nga para malaman ko kung ano ang pinag-uusapan nila"

    "..." "Filipino Leaders are corrupt and that they are upset about the recent appointment of Gen. Wood"

    person1 "(Gossiping) Nabalitaan niyo? Sinasabi nila na corrupt ang mga pilipino!"

    person2 "(Nodding) At ngayon itinalaga nila si General Wood."

    show mc thinking at right
    mc "(Listening intently) General Wood? Hindi ba siya yung  American gobernador-heneral?"

    "..." "(Chatter of multiple people discussing the \"anti-filipino\" report from Gen. Wood administration.)"

    person3 "(Joining the group) Nakita niyo ba ang bagong balita? Pinipinta tayo ng administrasyon ni Wood bilang anti-Filipino!"

    "..." "[mc] vividly remembering about Gen. Wood being an American governor-general and concludes that he is now in the American Era."

    mc "(Thinking)Ahh, ito pala ang panahon ng mga amerikano sa pilipinas."

    hide mc
    hide crowd
    show speaker
    Speaker "(Rising to speak) Mga kapwa ko Pilipino, hindi tayo maaaring manatiling nakatingin lang habang patuloy na inaapi ni Heneral Wood ang ating bayan!"
    Speaker "Panahon na para tayo ay magkaisa at labanan ang kawalang-katarungang ito nang buong lakas!"

    show mc realization at left
    mc "(Realizing the gravity of the situation) Paghihimagsik? Seryoso ito."
    hide mc
    mc "(Continuing to explore Manila) Ganito pala ang maynila sa panahon ng mga amerikano. Ibang-iba sa nakasanayan ko."

    #Scene 2
    scene bg street with fade
    "..." "the next day,[mc] goes to the same alley-way surprised to see that the number of people have doubled and that it had more important looking people."

    show mc speaking2 at left
    " [mc] (Inner monologue)"" hmmm… Sa sino sino kaya ang mga importanteng tao sa mga iyon? Siguro puro sila mga politiko…"

    "..." "It seemed that the Filipinos at the time decided to create a petition letter to address their grievances against Governor-General Leonard Wood."
    "..."  "The person writing the letter reads aloud as they write the letter."

    show mc default at left
    person4 "The first twenty years of civil government were marked by mutual understanding and loyal cooperation between American and Filipinos."
    person4 "At the end of that period, when it seemed that the goal had finally been reached."
    person4 "After the President of the United States had advised the Congress that the time had come for America to fulfill her sacred pledge."
    person4 "Major-General Leonard Wood was sent to the Philippines as Governor-General, Cognizant of the part taken by General Wood in the liberation of Cuba." 
    person4 "The Filipino people expected that under his administration the spirit of cooperation would be maintained and that the work of political emancipation would be complete."
    person4 "Contrary, however, to our expectations, his conduct of government has been characterized by a train of usurpations and arbitrary acts, resulting in the curtailment of our autonomy"
    person4 "The destruction of our constitutional system, and the reversal of America's Philippine policy."
    
    "..." "[mc] wonders for a bit and connects the pieces of the puzzle"
    show mc speaking2 at left
    mc "So ganun pala ang nangyari… lahat ng Filipino leaders ay galit kay general Wood sa kadahilanang, naibunyag nya ang mga corruption ng mga filipino leaders habang siya ay namamahala bilang governor-general."
    mc "Ang corruption na galing sa mga filipino leaders ay isang paghahanda para sa Philippine Independence." 
    show mc speaking at left
    mc "Pinalalawak nila ang kanilang kapangyarihan upang pagdating ng panahon ang pilipinas ay maging malaya pero sila ang mamamahala dito."
    
    "..." "After [mc]'s inner monologue he suddenly gets teleported and while within the time machine rift he realizes:"

    "[mc] (Inner Monologue)" "Ngayon ko lang na realize na nasa American Era of Philippine History pala ako…"

label subchapter2:
    #(CIA Intelligence Memorandum)
    #Scene1

    show bg black

    scene bg meeting with fade

    call slowTextfade("CIA Intelligence Memorandum")
    play music "music/bg_cia.mp3" fadein 0.5 volume 0.2 fadeout 0.5

    scene bg cia-table
    with fade
    
    show mc suit at center
    "..." "[mc] gets teleported in a dimly lit room where [mc] sees people in black suits having a meeting seated at a long rectangular table."
    "..."  "[mc] then looks around to realize that there are guards around the room and that [mc] outfit is similar to that of a guard."

    mc "(Looks around the place) Nasaan ako ngayon?. Parang may nagme-meeting na mga tao dito. Halos magkaparehas ba naman suot ko ng mga guwardiya dito."

    "..." "[mc] Looks up to the door and sees the logo of the CIA."

    mc " Parang nasa building ata ako ng CIA."
    
    menu:
        "It seems i'm inside the CIA building..."

        "Listen in on the meeting":
            jump textEvent7
        "This is dangerous I should get out of here":
            "[mc] (Inner thoughts)" "If i dont do this I wont be able to go home"
            jump textEvent7

label textEvent7:
    "..." "[mc] stands at the corner of a room acting as a guard."
    "..." "The meeting commences as a CIA executive opens with a stern tone."
    hide mc
    show executive default at left
    CIAExecutive "Gentlemen, we are gathered today to discuss a matter of national security."
    CIAExecutive "The spread of communism in Southeast Asia, particularly in the Philippines, poses a significant threat to American interests."
    CIAExecutive "To that end, we've compiled a report - CIA Memorandum 296 - detailing the current situation in the Philippines. "
    show mc suit at right
    mc "Nagsabi siya tungkol sa kumonismo? Kasabit ata ang Soviet Union dito. Pero saang bandang era kaya ako napadpad?"

    CIAExecutive "The Philippines, currently under President Quirino's administration, is plagued by corruption, political instability, and economic decline."
    CIAExecutive "This creates a breeding ground for communist influence."
    CIAExecutive "While our analysis suggests the next Philippine president will likely be a supporter of the US, the current downward spiral could lead to a communist takeover."
    
    "..." "CIA Executive divides the memorandum into three parts: Political, Economical, and Military Situation."

    CIAExecutive "Memorandum 296 is divided into three sections: Political, Economic, and Military. Let's begin with the political situation."
    CIAExecutive "The Filipino people are deeply dissatisfied with the Quirino administration. Corruption scandals have eroded public trust. Not only politicians, but wealthy landowners and those in power are lining their pockets."

    CIAExecutive "Now, the economic situation. The Philippines, a rich agricultural nation, should be self-sufficient in food production."
    CIAExecutive "However, long-standing inequalities in land ownership have fueled the rise of communist movements, particularly the Huks in Luzon, which are now spreading across the archipelago."

    CIAExecutive "The government's attempt to bolster the economy by raising taxes and restricting foreign trade backfired."
    CIAExecutive "Filipinos fear for their economic future, further deepening the political and economic instability."
    CIAExecutive "This inefficiency and corruption stem from a lack of education and political immaturity."

    CIAExecutive "The military situation is no better. Since the Cold War began, the Philippines has faced communist resistance from the Hukbalahap, or Huks."
    CIAExecutive "The overall instability weakens the Philippine Constabulary and Armed Forces, rendering them incapable of maintaining order."
    

    mc "(Realizes) Nasa panahon pala ako ng Cold War, pagkatapos ng Ikalawang Digmaang Pandaigdig. Medyo intense pa ang issue nito."

    CIAExecutive "The Huks were originally anti-Japanese militants who later embraced communism." 
    CIAExecutive "They're a rapidly growing guerilla force, well-equipped and supported by sympathetic villagers."
    CIAExecutive "Despite having better weapons, the Philippine military lacks strong leadership and motivation, making them ineffective against the Huks."
    
    mc "matagal na nakabaon ang korapsyon sa Pilipinas. Yan ay sanhi ng maraming problemang nangyari dito sa bansang ito."

    CIAExecutive "The agenda for this meeting has been already addressed and that no further discussion will occur. You are all dismissed."

    "..." "As the meeting ends, one guard notices [mc] presence and realizes they were not supposed to be there, prompting [mc] to flee."

    mc " (Realizing) Hala!! Nakita niya ako. Kailangan ko nang umalis dito!"

    "..." "[mc] runs towards the door and exits to another room."
    
    "..." "Just before the guard catches up, they are transported back to the time machine rift where they're nowhere to be seen."

    stop music
    scene bg black with fade
    call slowTextfade("While our main character is time travelling, the time machine short-circuited rendering our main character unconscious, giving them amnesia")
    scene bg black with fade
    call slowTextfade("Then the mc wakes up")
    scene bg campus dawn request

    "..." "(A school campus, in the middle of the field, around the crack of dawn)"

    "??? (In a daze)" "Uhmm…… What happened? Where am I?"

    pause (5)

    scene bg black
    call slowTextfade ("End")

    pause (5)

    $ renpy.full_restart()
