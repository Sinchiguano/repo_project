// Generated by gencpp from file industrial_extrinsic_cal/calibrationResult.msg
// DO NOT EDIT!


#ifndef INDUSTRIAL_EXTRINSIC_CAL_MESSAGE_CALIBRATIONRESULT_H
#define INDUSTRIAL_EXTRINSIC_CAL_MESSAGE_CALIBRATIONRESULT_H


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
struct calibrationResult_
{
  typedef calibrationResult_<ContainerAllocator> Type;

  calibrationResult_()
    : cost_per_observation(0.0)  {
    }
  calibrationResult_(const ContainerAllocator& _alloc)
    : cost_per_observation(0.0)  {
  (void)_alloc;
    }



   typedef double _cost_per_observation_type;
  _cost_per_observation_type cost_per_observation;





  typedef boost::shared_ptr< ::industrial_extrinsic_cal::calibrationResult_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::industrial_extrinsic_cal::calibrationResult_<ContainerAllocator> const> ConstPtr;

}; // struct calibrationResult_

typedef ::industrial_extrinsic_cal::calibrationResult_<std::allocator<void> > calibrationResult;

typedef boost::shared_ptr< ::industrial_extrinsic_cal::calibrationResult > calibrationResultPtr;
typedef boost::shared_ptr< ::industrial_extrinsic_cal::calibrationResult const> calibrationResultConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::industrial_extrinsic_cal::calibrationResult_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::industrial_extrinsic_cal::calibrationResult_<ContainerAllocator> >::stream(s, "", v);
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
struct IsFixedSize< ::industrial_extrinsic_cal::calibrationResult_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::industrial_extrinsic_cal::calibrationResult_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::industrial_extrinsic_cal::calibrationResult_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::industrial_extrinsic_cal::calibrationResult_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::industrial_extrinsic_cal::calibrationResult_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::industrial_extrinsic_cal::calibrationResult_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::industrial_extrinsic_cal::calibrationResult_<ContainerAllocator> >
{
  static const char* value()
  {
    return "e0512b76935b097d08145b35b180a039";
  }

  static const char* value(const ::industrial_extrinsic_cal::calibrationResult_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xe0512b76935b097dULL;
  static const uint64_t static_value2 = 0x08145b35b180a039ULL;
};

template<class ContainerAllocator>
struct DataType< ::industrial_extrinsic_cal::calibrationResult_<ContainerAllocator> >
{
  static const char* value()
  {
    return "industrial_extrinsic_cal/calibrationResult";
  }

  static const char* value(const ::industrial_extrinsic_cal::calibrationResult_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::industrial_extrinsic_cal::calibrationResult_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
# Define the result\n\
float64 cost_per_observation\n\
";
  }

  static const char* value(const ::industrial_extrinsic_cal::calibrationResult_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::industrial_extrinsic_cal::calibrationResult_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.cost_per_observation);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct calibrationResult_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::industrial_extrinsic_cal::calibrationResult_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::industrial_extrinsic_cal::calibrationResult_<ContainerAllocator>& v)
  {
    s << indent << "cost_per_observation: ";
    Printer<double>::stream(s, indent + "  ", v.cost_per_observation);
  }
};

} // namespace message_operations
} // namespace ros

#endif // INDUSTRIAL_EXTRINSIC_CAL_MESSAGE_CALIBRATIONRESULT_H
