#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2/2/15

@author: Sam Pfeiffer

This node sends a goal with a trick (yes, nods the head)
to test the play_motion_from_tts_feedback script.

"""
import rospy
from pal_interaction_msgs.msg import TtsGoal, TtsAction
from actionlib import SimpleActionClient

TTS_AS = "/tts"

if __name__ == '__main__':
    rospy.init_node('test_play_motion_from_tts_feedback_node')
    ac = SimpleActionClient(TTS_AS, TtsAction)
    rospy.loginfo("Trying to connect to: " + TTS_AS)
    connecting_tries = 0
    while not ac.wait_for_server(rospy.Duration(2.0)) and connecting_tries < 5:
    	rospy.logwarn("Retrying connecting to " + TTS_AS)
    	connecting_tries += 1
    if connecting_tries >= 5:
    	rospy.logerr("Couldn't connect to " + TTS_AS)
    	exit(0)

    tg = TtsGoal()
    tg.rawtext.text = 'I say yes <mark name="doTrick trickName=yes"/> and move my head'
    tg.rawtext.lang_id = "en_US"
    rospy.loginfo("Sending goal: " + str(tg))
    ac.send_goal_and_wait(tg)
    rospy.loginfo("Goal sent!")
    

# text: 
#   section: ''
#   key: ''
#   lang_id: ''
#   arguments: []
# rawtext: 
#   text: 'I say yes <mark name="doTrick trickName=yes"/> and move my head'
#   lang_id: 'en_US'
# speakerName: ''
# wait_before_speaking: 0.0