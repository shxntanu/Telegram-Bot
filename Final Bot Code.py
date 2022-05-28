import telegram
from telegram.ext import *
import responses as R
from datetime import datetime
from keep_alive import alive

# Making a bot object using the bot function and your bot's token

bot = telegram.Bot(token="<your bot token goes here>")

# Dictionary containing all Course outcomes of SPPU FE Subjects

co_dict = {"phy":'''Course Outcomes:

On completion of the course, learner will be able to–
CO1: Develop understanding of interference, diffraction and polarization; connect it to few
engineering applications.
CO2: Learn basics of lasers and optical fibers and their use in some applications.
CO3: Understand concepts and principles in quantum mechanics. Relate them to some
applications.
CO4: Understand theory of semiconductors and their applications in some semiconductor
devices.
CO5: Summarize basics of magnetism and superconductivity. Explore few of their
technological applications.
CO6: Comprehend use of concepts of physics for Non Destructive Testing. Learn some
properties of nanomaterials and their application.''',

"bee":'''Course Outcomes:

At the end of course students will be able to
CO1: Differentiate between electrical and magnetic circuits and derive mathematical relation for
self and mutual inductance along with coupling effect.
CO2: Calculate series, parallel and composite capacitor as well as characteristics parameters of
alternating quantity and phasor arithmetic
CO3: Derive expression for impedance, current, power in series and parallel RLC circuit with AC
supply along with phasor diagram.
CO4: Relate phase and line electrical quantities in polyphase networks, demonstrate the operation
of single phase transformer and calculate efficiency and regulation at different loading conditions
CO5: Apply and analyze the resistive circuits using star-delta conversion KVL, KCL and different
network theorems under DC supply.
CO6: Evaluate work, power, energy relations and suggest various batteries for different
applications, concept of charging and discharging and depth of charge.''',

"pps":'''Course Outcomes:

On completion of the course, learner will be able to–
CO1: Inculcate and apply various skills in problem solving.
CO2: Choose most appropriate programming constructs and features to solve the problems in
diversified domains.
CO3: Exhibit the programming skills for the problems those require the writing of welldocumented programs including use of the logical constructs of language, Python.
CO4: Demonstrate significant experience with the Python program development environment.''',

"em2":'''Course Outcomes (COs): 

The students will be able to learn
CO1: the effective mathematical tools for solutions of first order differential equations that model
physical processes such as Newton’s law of cooling, electrical circuit, rectilinear motion, mass spring
systems, heat transfer etc.
CO2: advanced integration techniques such as Reduction formulae, Beta functions, Gamma
functions, Differentiation under integral sign and Error functions needed in evaluating multiple
integrals and their applications.
CO3: to trace the curve for a given equation and measure arc length of various curves.
CO4: the concepts of solid geometry using equations of sphere, cone and cylinder in a
comprehensive manner.
CO5: evaluation of multiple integrals and its application to find area bounded by curves, volume
bounded by surfaces, Centre of gravity and Moment of inertia.
''',

"chem":'''Course Outcomes:

On completion of the course, learner will be able to–
CO1: Apply the different methodologies for analysis of water and techniques involved in softening
of water as commodity.
CO2: Select appropriate electro-technique and method of material analysis.
CO3: Demonstrate the knowledge of advanced engineering materials for various engineering
applications.
CO4: Analyze fuel and suggest use of alternative fuels.
CO5: Identify chemical compounds based on their structure.
CO6: Explain causes of corrosion and methods for minimizing corrosion.''',

"bxe":'''Course Outcomes: 

On completion of the course, learner will be able to–
CO1: Explain the working of P-N junction diode and its circuits.
CO2: Identify types of diodes and plot their characteristics and also can compare BJT with
MOSFET.
CO3: Build and test analog circuits using OPAMP and digital circuits using universal/basic gates
and flip flops.
CO4: Use different electronics measuring instruments to measure various electrical parameters.
CO5: Select sensors for specific applications.
CO6: Describe basic principles of communication systems.''',

"em":'''Course Outcomes:

On completion of the course, learner will be able to–
CO1: Determine resultant of various force systems
CO2: Determine centroid, moment of inertia and solve problems related to friction
CO3:Determine reactions of beams, calculate forces in cables using principles of equilibrium
CO4: Solve trusses, frames for finding member forces and apply principles of equilibrium to
forces in space
CO5: Calculate position, velocity and acceleration of particle using principles of kinematics
CO6: Calculate position, velocity and acceleration of particle using principles of kinetics and
Work, Power, Energy
''',

"eg":'''Course Outcomes:

On completion of the course, learner will be able to
CO1: Draw the fundamental engineering objects using basic rules and able to construct the simple
geometries.
CO2: Construct the various engineering curves using the drawing instruments.
CO3: Apply the concept of orthographic projection of an object to draw several 2D views and its
sectional views for visualizing the physical state of the object.
CO4: Apply the visualization skill to draw a simple isometric projection from given orthographic
views precisely using drawing equipment.
CO5: Draw the development of lateral surfaces for cut section of geometrical solids.
CO6: Draw fully-dimensioned 2D, 3D drawings using computer aided drafting tools.''',

"pbl":'''Course Outcomes:

CO1: Project based learning will increase their capacity and learning through shared cognition.
CO2: Students able to draw on lessons from several disciplines and apply them in practical way.
CO3: Learning by doing approach in PBL will promote long-term retention of material and
replicable skill, as well as improve teachers' and students' attitudes towards learning.''',

"es2":'''Course Outcomes:

On completion of the course, learner will be able to–
CO1: Have an understanding of environmental pollution and the science behind those problems
and potential solutions.
CO2: Have knowledge of various acts and laws and will be able to identify the industries that are
violating these rules.
CO3: Assess the impact of ever increasing human population on the biosphere: social, economic
issues and role of humans in conservation of natural resources.
CO4: Learn skills required to research and analyze environmental issues scientifically and learn
how to use those skills in applied situations such as careers that may involve environmental
problems and/or issues.'''}


print(
    "\n\n------------------------------------------------------------------------------------------------------------------\n\nBot started!!"
)

updates = bot.get_updates()

# Sample Command which checks if the bot is online

def start_command(update, context):
    update.message.reply_text('Type something random to get started')

# Help command which describes the bot and its commands

def help_command(update, context):
    update.message.reply_text(
        '''Hola!
This bot is still in developmental stage, but it does have a few commands that you can use :) 

/start - A test command to see if the bot is online 
/help - A command to see all the commands available for the bot
/time - Tells you the current time 
/timetable - To fetch the timetable of any division 
/vision - Vision of PICT 
/mission - Mission of PICT 
/courseoutcome - Shows the course outcomes of each subject of Second Semester in FE
/books - link for the required FE books

 Then there come some commands which don't need a Slash to operate:
hi - The bot greets you with a message 
about - A little description about the bot :)'''
    )

# Time command which tells the current time (Note: if the bot is running on a server, then it'll tell the time of the server)

def time(update, context):
    update.message.reply_text(
        str((datetime.now()).strftime("%d/%m/%y %H:%M:%S")))

# Command to get the link of the telegram channel with SPPU books

def books(update,context):
    update.message.reply_text('''The following telegram channel has the books you need:
    
                        https://t.me/pictfebookssem2''')

# Command to show the vision of PICT

def vision(update, context):
    update.message.reply_text(
        "Vision:\n\nPune Institute of Computer Technology aspires to be the leader in Higher technical education and research of International repute."
    )

# Command to show the mission of PICT

def mission(update, context):
    update.message.reply_text(
        "Mission:\n\nTo be the leading and the most sought after institute of education and research in emerging engineering and technology disciplines that attract, retains and sustains gifted individuals of significant potential."
    )

# Command which sends you the message syntax to obtain the course outcomes of the desired subjects in the SPPU Syllabus

def course_outcomes(update,context):
    update.message.reply_text('''Hey there!
You really need to memorise the CO's of subjects, don't you? 😂

To get the CO's of subjects, follow the following syntax:


                                 co <space> <subject name>

where subject names: EM2, PHY, CHEM, EG, BEE, BXE, EM, PPS, ES2

Enjoy!''')

# Command which sends you the message syntax to obtain the timetable of any FE division in PICT

def timetable(update, context):
    update.message.reply_text(
        '''Hey there PICTian 🌊,\nTo get the timetable for the required division, type a command in the following manner.\n\nSyntax:\n
                        tt <space> x\n\nwhere x: Number of the division whose timetable you want to fetch.
    Enjoy!
    ''')

# Function to handle messages

def handle_message(update, context):
    text = str(update.message.text).lower()
    
    if text in ("tt 1", "tt 2", "tt 3", "tt 4", "tt 5", "tt 6", "tt 7", "tt 8",
                "tt 9", "tt 10", "tt 11"):
        sl = list(text.split(" "))
        bot.send_photo(
            update.message.chat.id,
            'https://pict-tt-bot.vercel.app/FE%20({}).jpg'.format(str(sl[1])))

    elif text in ("co eg", "co bxe","co em","co pps","co chem","co phy","co em2","co es2"):
        sl = list(text.split())
        bot.send_message(update.message.chat.id, co_dict[str(sl[1])])
  
    elif text in ("waah"):
        bot.send_photo(update.message.chat_id, 'https://i.ibb.co/zfz9kKb/waah-emote.png')
        bot.delete_message(update.message.chat_id, update.message.message_id)
    
    elif text in ("pepelaugh"):
        bot.send_sticker(update.message.chat_id, 'CAACAgIAAxkBAAEURmtii0iY-KuGVeKyUJoTxp2YMb5BHwACrCsAAktqAwABR84tu7AWggMkBA')
        bot.delete_message(update.message.chat_id, update.message.message_id)

    elif text in ("pepehands"):
      bot.send_sticker(update.message.chat_id, 'CAACAgIAAxkBAAEUZR1ij7RPt7mIFToH39QDIVzzFDSi4gAC-SYAAktqAwABJKWBkTWlpzokBA')

    elif text in ("ez"):
      bot.send_sticker(update.message.chat_id,'CAACAgIAAxkBAAEUZSVij7cZuSIxNJENYO0M5IZOmf090wACOyYAAktqAwABU3EJXSaKHCQkBA')

    elif text in ("monkas"):
      bot.send_sticker(update.message.chat_id,'CAACAgIAAxkBAAEUZS1ij7e2_nSsC8CFUp-5UrnW-fnD4wACMyYAAktqAwABf5ROt-qqdcYkBA')

    elif text in ("feelsbadman"):
      bot.send_sticker(update.message.chat_id,'CAACAgIAAxkBAAEUZTFij7f2D7p3Qdw74eYLY3nFarsqdQACMSYAAktqAwAB5LUCSor2LWUkBA')
      bot.delete_message(update.message.chat_id,update.message.message_id)
      
  
    elif text in ("haraami","harami"):
        bot.send_sticker(update.message.chat_id, 'CAACAgUAAxkBAAEURqhii1LslqS5XtbcNy4qUFuS7ALlFgACRgIAAsAs6FcKRb3LSnXQnyQE')
        bot.delete_message(update.message.chat_id, update.message.message_id)
    
    else:
        response = R.sample_responses(text)
        update.message.reply_text(response)

# Function to see errors

def error(update, context):
    print(f"Update {update} caused error {context.error}")

# Main function

def main():
    alive()
    updater = Updater("your bot token goes here",use_context=True)
    dp = updater.dispatcher

    # Command Handlers

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("time", time))
    dp.add_handler(CommandHandler("timetable", timetable))
    dp.add_handler(CommandHandler("vision", vision))
    dp.add_handler(CommandHandler("mission", mission))
    dp.add_handler(CommandHandler("courseoutcome",course_outcomes))
    dp.add_handler(CommandHandler("books",books))
    
    # Message Handler

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()
