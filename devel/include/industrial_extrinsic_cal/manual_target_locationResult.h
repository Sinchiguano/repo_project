// Generated by gencpp from file industrial_extrinsic_cal/manual_target_locationResult.msg
// DO NOT EDIT!


#ifndef INDUSTRIAL_EXTRINSIC_CAL_MESSAGE_MANUAL_TARGET_LOCATIONRESULT_H
#define INDUSTRIAL_EXTRINSIC_CAL_MESSAGE_MANUAL_TARGET_LOCATIONRESULT_H


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
struct manual_target_locationResult_
{
  typedef manual_target_locationResult_<ContainerAllocator> Type;

  manual_target_locationResult_()
    : result(0)  {
    }
  manual_target_locationResult_(const ContainerAllocator& _alloc)
    : result(0)  {
  (void)_alloc;
    }



   typedef uint32_t _result_type;
  _result_type result;





  typedef boost::shared_ptr< ::industrial_extrinsic_cal::manual_target_locationResult_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::industrial_extrinsic_cal::manual_target_locationResult_<ContainerAllocator> const> ConstPtr;

}; // struct manual_target_locationResult_

typedef ::industrial_extrinsic_cal::manual_target_locationResult_<std::allocator<void> > manual_target_locationResult;

typedef boost::shared_ptr< ::industrial_extrinsic_cal::manual_target_locationResult > manual_target_locationResultPtr;
typedef boost::shared_ptr< ::industrial_extrinsic_cal::manual_target_locationResult const> manual_target_locationResultConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::industrial_extrinsic_cal::manual_target_locationResult_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::industrial_extrinsic_cal::manual_target_locationResult_<ContainerAllocator> >::stream(s, "", v);
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
struct IsFixedSize< ::industrial_extrinsic_cal::manual_target_locationResult_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::industrial_extrinsic_cal::manual_target_locationResult_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::industrial_extrinsic_cal::manual_target_locationResult_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::industrial_extrinsic_cal::manual_target_locationResult_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::industrial_extrinsic_cal::manual_target_locationResult_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::industrial_extrinsic_cal::manual_target_locationResult_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::industrial_extrinsic_cal::manual_target_locationResult_<ContainerAllocator> >
{
  static const char* value()
  {
    return "13d5d28ceaaadbc975dd072a2e10b88a";
  }

  static const char* value(const ::industrial_extrinsic_cal::manual_target_locationResult_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x13d5d28ceaaadbc9ULL;
  static const uint64_t static_value2 = 0x75dd072a2e10b88aULL;
};

template<class ContainerAllocator>
struct DataType< ::industrial_extrinsic_cal::manual_target_locationResult_<ContainerAllocator> >
{
  static const char* value()
  {
    return "industrial_extrinsic_cal/manual_target_locationResult";
  }

  static const char* value(const ::industrial_extrinsic_cal::manual_target_locationResult_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::industrial_extrinsic_cal::manual_target_locationResult_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
# Define the result\n\
uint32 result  # just a placeholder\n\
";
  }

  static const char* value(const ::industrial_extrinsic_cal::manual_target_locationResult_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::industrial_extrinsic_cal::manual_target_locationResult_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.result);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct manual_target_locationResult_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::industrial_extrinsic_cal::manual_target_locationResult_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::industrial_extrinsic_cal::manual_target_locationResult_<ContainerAllocator>& v)
  {
    s << indent << "result: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.result);
  }
};

} // namespace message_operations
} // namespace ros

#endif // INDUSTRIAL_EXTRINSIC_CAL_MESSAGE_MANUAL_TARGET_LOCATIONRESULT_H
