#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from flexbe_manipulation_states.moveit_to_joints_dyn_state import MoveitToJointsDynState as flexbe_manipulation_states__MoveitToJointsDynState
from hrwros_factory_states.compute_grasp_state import ComputeGraspState
from hrwros_factory_states.detect_part_camera_state import DetectPartCameraState
from hrwros_factory_states.set_conveyor_power_state import SetConveyorPowerState
from hrwros_factory_states.vacuum_gripper_control_state import VacuumGripperControlState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Sat Aug 05 2023
@author: Swaraj Anil Zende
'''
class PickPartfromConveyerSM(Behavior):
	'''
	This is behaviour for the hrwros_factory simulation that picks a part from the conveyer belt using Robot1
	'''


	def __init__(self):
		super(PickPartfromConveyerSM, self).__init__()
		self.name = 'Pick Part from Conveyer'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		pick_group = 'robot1'
		home1 = [1.57,-1.57,1.24,-1.57,-1.57,0]
		gripper1 = 'vacuum_gripper1_suction_cup'
		names1 = ['robot1_elbow_joint','robot1_shoulder_lift_joint','robot1_shoulder_pan_joint','robot1_wrist_1_joint', 'robot1_wrist_2_joint', 'robot1_wrist_3_joint']
		# x:736 y:616, x:56 y:531
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.part_pose = {}
		_state_machine.userdata.pick_configuration = []
		_state_machine.userdata.home1 = home1
		_state_machine.userdata.Conveyer_speed = 100

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:27 y:29
			OperatableStateMachine.add('Start_Conveyer',
										SetConveyorPowerState(stop=False),
										transitions={'succeeded': 'Detect Part', 'failed': 'failed'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'speed': 'Conveyer_speed'})

			# x:534 y:251
			OperatableStateMachine.add('Compute pick configuration',
										ComputeGraspState(group=pick_group, offset=0.0, joint_names=names1, tool_link=gripper1, rotation=3.1415),
										transitions={'continue': 'Move Robot1 to pick', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'pose': 'part_pose', 'joint_values': 'pick_configuration', 'joint_names': 'joint_names'})

			# x:203 y:91
			OperatableStateMachine.add('Detect Part',
										DetectPartCameraState(ref_frame='robot1_base', camera_topic='/hrwros/logical_camera_1', camera_frame='logical_camera_1_frame'),
										transitions={'continue': 'Stop_Conveyer', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'pose': 'part_pose'})

			# x:821 y:520
			OperatableStateMachine.add('Move Robot1 to Home configuration',
										flexbe_manipulation_states__MoveitToJointsDynState(move_group=pick_group, action_topic='/move_group'),
										transitions={'reached': 'finished', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'home1', 'joint_names': 'joint_names'})

			# x:678 y:335
			OperatableStateMachine.add('Move Robot1 to pick',
										flexbe_manipulation_states__MoveitToJointsDynState(move_group=pick_group, action_topic='/move_group'),
										transitions={'reached': 'Activate Gripper', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'pick_configuration', 'joint_names': 'joint_names'})

			# x:447 y:132
			OperatableStateMachine.add('Stop_Conveyer',
										SetConveyorPowerState(stop=True),
										transitions={'succeeded': 'Compute pick configuration', 'failed': 'failed'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'speed': 'Conveyer_speed'})

			# x:824 y:425
			OperatableStateMachine.add('Activate Gripper',
										VacuumGripperControlState(enable=True, service_name='/gripper1/control'),
										transitions={'continue': 'Move Robot1 to Home configuration', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
