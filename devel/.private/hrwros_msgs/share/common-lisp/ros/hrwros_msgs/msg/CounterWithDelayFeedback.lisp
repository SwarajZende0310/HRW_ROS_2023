; Auto-generated. Do not edit!


(cl:in-package hrwros_msgs-msg)


;//! \htmlinclude CounterWithDelayFeedback.msg.html

(cl:defclass <CounterWithDelayFeedback> (roslisp-msg-protocol:ros-message)
  ((counts_elapsed
    :reader counts_elapsed
    :initarg :counts_elapsed
    :type cl:integer
    :initform 0))
)

(cl:defclass CounterWithDelayFeedback (<CounterWithDelayFeedback>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <CounterWithDelayFeedback>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'CounterWithDelayFeedback)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name hrwros_msgs-msg:<CounterWithDelayFeedback> is deprecated: use hrwros_msgs-msg:CounterWithDelayFeedback instead.")))

(cl:ensure-generic-function 'counts_elapsed-val :lambda-list '(m))
(cl:defmethod counts_elapsed-val ((m <CounterWithDelayFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader hrwros_msgs-msg:counts_elapsed-val is deprecated.  Use hrwros_msgs-msg:counts_elapsed instead.")
  (counts_elapsed m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <CounterWithDelayFeedback>) ostream)
  "Serializes a message object of type '<CounterWithDelayFeedback>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'counts_elapsed)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'counts_elapsed)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'counts_elapsed)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'counts_elapsed)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <CounterWithDelayFeedback>) istream)
  "Deserializes a message object of type '<CounterWithDelayFeedback>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'counts_elapsed)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'counts_elapsed)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'counts_elapsed)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'counts_elapsed)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<CounterWithDelayFeedback>)))
  "Returns string type for a message object of type '<CounterWithDelayFeedback>"
  "hrwros_msgs/CounterWithDelayFeedback")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'CounterWithDelayFeedback)))
  "Returns string type for a message object of type 'CounterWithDelayFeedback"
  "hrwros_msgs/CounterWithDelayFeedback")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<CounterWithDelayFeedback>)))
  "Returns md5sum for a message object of type '<CounterWithDelayFeedback>"
  "cca3cfadafd90f6c2989b5f5e521eb59")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'CounterWithDelayFeedback)))
  "Returns md5sum for a message object of type 'CounterWithDelayFeedback"
  "cca3cfadafd90f6c2989b5f5e521eb59")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<CounterWithDelayFeedback>)))
  "Returns full string definition for message of type '<CounterWithDelayFeedback>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%uint32 counts_elapsed		# Feedback message: number of counts elapsed.~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'CounterWithDelayFeedback)))
  "Returns full string definition for message of type 'CounterWithDelayFeedback"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%uint32 counts_elapsed		# Feedback message: number of counts elapsed.~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <CounterWithDelayFeedback>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <CounterWithDelayFeedback>))
  "Converts a ROS message object to a list"
  (cl:list 'CounterWithDelayFeedback
    (cl:cons ':counts_elapsed (counts_elapsed msg))
))
