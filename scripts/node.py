#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 27/11/14

@author: Sam Pfeiffer

This node subscribes to the /tts/feedback
and executes whatever movement is sent when
id: doTrick trickName=bow
appears.

"""
import rospy
from pal_interaction_msgs.msg import TtsActionFeedback
from play_motion_msgs.msg import PlayMotionActionGoal


TTS_FEEDBACK_TOPIC = "/tts/feedback"
PLAY_MOTION_GOAL_TOPIC = "/play_motion/goal"



class PM_from_TTS():
    def __init__(self):
        rospy.loginfo("Setting publisher to: " + PLAY_MOTION_GOAL_TOPIC)
        self.pm_pub = rospy.Publisher(PLAY_MOTION_GOAL_TOPIC, PlayMotionActionGoal)
        rospy.loginfo("Subscribing to: " + TTS_FEEDBACK_TOPIC)
        self.tts_sub = rospy.Subscriber(TTS_FEEDBACK_TOPIC, TtsActionFeedback, self.tts_fdbk_cb)
        rospy.loginfo("Ready to work.")


    def tts_fdbk_cb(self, data):
        rospy.loginfo("Received cb with:\n  text_said: " +
                       str(data.feedback.text_said) +
                       "\n  marks.id: " +str(data.feedback.marks.id))
        #data = TtsActionFeedback()
        if "doTrick trickName=" in data.feedback.marks.id:
            rospy.loginfo("Found trigger: " + str(data.feedback.marks.id))
            motion_name = data.feedback.marks.id.replace("doTrick trickName=", "")
            motion_name = motion_name.split()[0] # In case there are more params
            # doTrick trickName=minidance checkSafety=0 #like in this case
            pmag = PlayMotionActionGoal()
            pmag.goal.motion_name = motion_name
            pmag.goal.skip_planning = False
            rospy.logwarn("Sending play_motion goal: " + str(motion_name))
            self.pm_pub.publish(pmag)
        

if __name__ == '__main__':
    rospy.init_node('play_motion_from_tts_feedback_node')

    node = PM_from_TTS()
    rospy.spin()
# header: 
#   seq: 407
#   stamp: 
#     secs: 1417079926
#     nsecs: 6335802
#   frame_id: ''
# status: 
#   goal_id: 
#     stamp: 
#       secs: 1417079925
#       nsecs: 912096603
#     id: /tts-9-1417079925.912096603
#   status: 1
#   text: This goal has been accepted by the simple action server
# feedback: 
#   event_type: 16
#   timestamp: 
#     secs: 0
#     nsecs: 0
#   text_said: ''
#   next_word: ''
#   marks: 
#     id: doTrick trickName=bow
#     keys: []
#     value: []