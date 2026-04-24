#!/usr/bin/env python

from moveit_commander import MoveGroupCommander
from geometry_msgs.msg import Pose
from geometry_msgs.msg import PoseStamped
import rospy
import tf

def main():

    rospy.init_node("moveit_command_sender")
    panda_arm = MoveGroupCommander("panda_arm")
    initial_reference_frame = panda_arm.get_pose_reference_frame()
    rospy.loginfo(" Initial Reference Frame: {}".format(initial_reference_frame))
    initial_pose = panda_arm.get_current_pose()
    rospy.loginfo("Initial Pose:\n{}".format(initial_pose))


    # heatpress target
    rospy.loginfo("Start heatpress manipulation")

    # Relative Target Pose
    target_posestamped = PoseStamped()
    target_posestamped.pose.position.x = 0.3
    target_posestamped.pose.position.y = 0.0
    target_posestamped.pose.position.z = 0.68
    target_posestamped.pose.orientation.x = 1.0
    target_posestamped.header.frame_id = '/world'
    target_posestamped.header.stamp = rospy.Time.now()
    rospy.loginfo("Target Posestamped:\n{}".format(target_posestamped))

    panda_arm.set_pose_target(target_posestamped)
    panda_arm.go()


    # heatpress target2
    rospy.loginfo("Start heatpress manipulation 2")

    # use pose and reference frame
    panda_arm.set_pose_reference_frame('/HEATPRESS_BODY')
    rospy.loginfo("Current Reference Frame: {}".format(panda_arm.get_pose_reference_frame()))
    target_pose = Pose()
    target_pose.position.x = 0.3
    target_pose.position.y = 0.0
    target_pose.position.z = 0.68
    target_pose.orientation.x = 1.0
    rospy.loginfo("Target Pose:\n{}".format(target_pose))

    #panda_arm.set_pose_target(target_pose)
    #panda_arm.go()


    # heatpress target3. use get_current_target_pose
    rospy.loginfo("Start heatpress manipulation 3")

    # Frame ID Definitions
    planning_frame_id = panda_arm.get_planning_frame()
    heatpress_frame_id = '/HEATPRESS_BODY'
    coldpress_frame_id = '/COLDPRESS_BODY'
    cutter_frame_id = '/CUTTER_BODY'
    wscale_frame_id = '/WEIGHING-SCALE_BODY'

    # Get a target pose
    target_pose_heatpress = get_current_target_pose(heatpress_frame_id, planning_frame_id)
    target_pose_coldpress = get_current_target_pose(coldpress_frame_id, planning_frame_id)
    target_pose_cutter = get_current_target_pose(cutter_frame_id, planning_frame_id)
    target_pose_wscale = get_current_target_pose(wscale_frame_id, planning_frame_id)

    # weighing scale
    rospy.loginfo("Weighing scale manipulation")
    if target_pose_wscale:
        target_pose_wscale.pose.position.x -= 0.3
        target_pose_wscale.pose.position.y -= 0.0
        target_pose_wscale.pose.position.z += 0.15
        target_pose_wscale.pose.orientation.x = 1.0
        target_pose_wscale.pose.orientation.y = 0.0
        target_pose_wscale.pose.orientation.z = 0.0
        target_pose_wscale.pose.orientation.w = 0.0
        rospy.loginfo("Set Target To:\n{}".format(target_pose_wscale))
        panda_arm.set_pose_target(target_pose_wscale)
        ret = panda_arm.go()
        rospy.loginfo("Executed ... {}".format(ret))
    else:
        rospy.loginfo("Pose Error: {}".format(target_pose_wscale))

    # heatpress
    rospy.loginfo("Heatpress manipulation")
    if target_pose_heatpress:
        target_pose_heatpress.pose.position.y -= 0.3
        target_pose_heatpress.pose.position.z += 0.6
        target_pose_heatpress.pose.orientation.x = 1.0
        target_pose_heatpress.pose.orientation.y = 0.0
        target_pose_heatpress.pose.orientation.z = 0.0
        target_pose_heatpress.pose.orientation.w = 0.0
        rospy.loginfo("Set Target To:\n{}".format(target_pose_heatpress))
        panda_arm.set_pose_target(target_pose_heatpress)
        ret = panda_arm.go()
        rospy.loginfo("Executed ... {}".format(ret))
    else:
        rospy.loginfo("Pose Error: {}".format(target_pose_heatpress))

    # coldpress
    rospy.loginfo("Coldpress manipulation")
    if target_pose_coldpress:
        target_pose_coldpress.pose.position.x += 0.3
        target_pose_coldpress.pose.position.y -= 0.4
        target_pose_coldpress.pose.position.z += 0.6
        target_pose_coldpress.pose.orientation.x = 1.0
        target_pose_coldpress.pose.orientation.y = 0.0
        target_pose_coldpress.pose.orientation.z = 0.0
        target_pose_coldpress.pose.orientation.w = 0.0
        rospy.loginfo("Set Target To:\n{}".format(target_pose_coldpress))
        panda_arm.set_pose_target(target_pose_coldpress)
        ret = panda_arm.go()
        rospy.loginfo("Executed ... {}".format(ret))
    else:
        rospy.loginfo("Pose Error: {}".format(target_pose_coldpress))



def get_current_target_pose(target_frame_id, base_frame_id, timeout = 1.0):

    endtime = rospy.get_time()
    rospy.loginfo( "Waiting Clock: {}".format(endtime))
    while not endtime:
        endtime = rospy.get_time()

    endtime += timeout

    target_pose = None
    listener = tf.TransformListener()
    rate = rospy.Rate(10.0)

    while not rospy.is_shutdown():
        try:
            now = rospy.Time(0)
            (trans,quat) = listener.lookupTransform(base_frame_id, target_frame_id, now)
            target_pose = PoseStamped()
            target_pose.pose.position.x = trans[0]
            target_pose.pose.position.y = trans[1]
            target_pose.pose.position.z = trans[2]
            target_pose.pose.orientation.x = quat[0]
            target_pose.pose.orientation.y = quat[1]
            target_pose.pose.orientation.z = quat[2]
            target_pose.pose.orientation.w = quat[3]
            target_pose.header.frame_id = base_frame_id
            target_pose.header.stamp = now
            break
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException) as e:
            rospy.logwarn(e)

        now_float = rospy.get_time()
        if endtime < now_float:
            rospy.logwarn("Time Out: {} [sec] at Clock: {} [sec]".format(timeout, now_float))
            break

        rate.sleep()

    return target_pose


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
