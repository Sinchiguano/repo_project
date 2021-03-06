// Generated by gencpp from file robo_cylinder/MoveMeters.msg
// DO NOT EDIT!


#ifndef ROBO_CYLINDER_MESSAGE_MOVEMETERS_H
#define ROBO_CYLINDER_MESSAGE_MOVEMETERS_H

#include <ros/service_traits.h>


#include <robo_cylinder/MoveMetersRequest.h>
#include <robo_cylinder/MoveMetersResponse.h>


namespace robo_cylinder
{

struct MoveMeters
{

typedef MoveMetersRequest Request;
typedef MoveMetersResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct MoveMeters
} // namespace robo_cylinder


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::robo_cylinder::MoveMeters > {
  static const char* value()
  {
    return "6f982fc36fa004e803e69f0803390fad";
  }

  static const char* value(const ::robo_cylinder::MoveMeters&) { return value(); }
};

template<>
struct DataType< ::robo_cylinder::MoveMeters > {
  static const char* value()
  {
    return "robo_cylinder/MoveMeters";
  }

  static const char* value(const ::robo_cylinder::MoveMeters&) { return value(); }
};


// service_traits::MD5Sum< ::robo_cylinder::MoveMetersRequest> should match 
// service_traits::MD5Sum< ::robo_cylinder::MoveMeters > 
template<>
struct MD5Sum< ::robo_cylinder::MoveMetersRequest>
{
  static const char* value()
  {
    return MD5Sum< ::robo_cylinder::MoveMeters >::value();
  }
  static const char* value(const ::robo_cylinder::MoveMetersRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::robo_cylinder::MoveMetersRequest> should match 
// service_traits::DataType< ::robo_cylinder::MoveMeters > 
template<>
struct DataType< ::robo_cylinder::MoveMetersRequest>
{
  static const char* value()
  {
    return DataType< ::robo_cylinder::MoveMeters >::value();
  }
  static const char* value(const ::robo_cylinder::MoveMetersRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::robo_cylinder::MoveMetersResponse> should match 
// service_traits::MD5Sum< ::robo_cylinder::MoveMeters > 
template<>
struct MD5Sum< ::robo_cylinder::MoveMetersResponse>
{
  static const char* value()
  {
    return MD5Sum< ::robo_cylinder::MoveMeters >::value();
  }
  static const char* value(const ::robo_cylinder::MoveMetersResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::robo_cylinder::MoveMetersResponse> should match 
// service_traits::DataType< ::robo_cylinder::MoveMeters > 
template<>
struct DataType< ::robo_cylinder::MoveMetersResponse>
{
  static const char* value()
  {
    return DataType< ::robo_cylinder::MoveMeters >::value();
  }
  static const char* value(const ::robo_cylinder::MoveMetersResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // ROBO_CYLINDER_MESSAGE_MOVEMETERS_H
