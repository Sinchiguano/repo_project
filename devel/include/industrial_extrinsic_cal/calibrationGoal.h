// Generated by gencpp from file industrial_extrinsic_cal/calibrationGoal.msg
// DO NOT EDIT!


#ifndef INDUSTRIAL_EXTRINSIC_CAL_MESSAGE_CALIBRATIONGOAL_H
#define INDUSTRIAL_EXTRINSIC_CAL_MESSAGE_CALIBRATIONGOAL_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace industrial_extrinsic_cal
{
template <class ContainerAllocator>
struct calibrationGoal_
{
  typedef calibrationGoal_<ContainerAllocator> Type;

  calibrationGoal_()
    : allowable_cost_per_observation(0.0)  {
    }
  calibrationGoal_(const ContainerAllocator& _alloc)
    : allowable_cost_per_observation(0.0)  {
  (void)_alloc;
    }



   typedef double _allowable_cost_per_observation_type;
  _allowable_cost_per_observation_type allowable_cost_per_observation;





  typedef boost::shared_ptr< ::industrial_extrinsic_cal::calibrationGoal_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::industrial_extrinsic_cal::calibrationGoal_<ContainerAllocator> const> ConstPtr;

}; // struct calibrationGoal_

typedef ::industrial_extrinsic_cal::calibrationGoal_<std::allocator<void> > calibrationGoal;

typedef boost::shared_ptr< ::industrial_extrinsic_cal::calibrationGoal > calibrationGoalPtr;
typedef boost::shared_ptr< ::industrial_extrinsic_cal::calibrationGoal const> calibrationGoalConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::industrial_extrinsic_cal::calibrationGoal_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::industrial_extrinsic_cal::calibrationGoal_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace industrial_extrinsic_cal

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'sensor_msgs': ['/opt/ros/kinetic/share/sensor_msgs/cmake/../msg'], 'actionlib_msgs': ['/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg'], 'industrial_extrinsic_cal': ['/home/casch/yumi_depends_ws/devel/share/industrial_extrinsic_cal/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::industrial_extrinsic_cal::calibrationGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::industrial_extrinsic_cal::calibrationGoal_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::industrial_extrinsic_cal::calibrationGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::industrial_extrinsic_cal::calibrationGoal_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::industrial_extrinsic_cal::calibrationGoal_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::industrial_extrinsic_cal::calibrationGoal_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::industrial_extrinsic_cal::calibrationGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "018b5c6376abafbce2c3211a0d675d06";
  }

  static const char* value(const ::industrial_extrinsic_cal::calibrationGoal_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x018b5c6376abafbcULL;
  static const uint64_t static_value2 = 0xe2c3211a0d675d06ULL;
};

template<class ContainerAllocator>
struct DataType< ::industrial_extrinsic_cal::calibrationGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "industrial_extrinsic_cal/calibrationGoal";
  }

  static const char* value(const ::industrial_extrinsic_cal::calibrationGoal_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::industrial_extrinsic_cal::calibrationGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
# Define the goal\n\
float64 allowable_cost_per_observation\n\
";
  }

  static const char* value(const ::industrial_extrinsic_cal::calibrationGoal_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::industrial_extrinsic_cal::calibrationGoal_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.allowable_cost_per_observation);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct calibrationGoal_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::industrial_extrinsic_cal::calibrationGoal_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::industrial_extrinsic_cal::calibrationGoal_<ContainerAllocator>& v)
  {
    s << indent << "allowable_cost_per_observation: ";
    Printer<double>::stream(s, indent + "  ", v.allowable_cost_per_observation);
  }
};

} // namespace message_operations
} // namespace ros

#endif // INDUSTRIAL_EXTRINSIC_CAL_MESSAGE_CALIBRATIONGOAL_H
