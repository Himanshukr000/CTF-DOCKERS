<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt"%>
<%@ taglib prefix="fn" uri="http://java.sun.com/jsp/jstl/functions"%>
<%@ taglib uri="http://www.springframework.org/tags/form" prefix="form" %>  
<%
	String path = request.getContextPath();
	String basePath = request.getScheme() + "://"
			+ request.getServerName() + ":" + request.getServerPort()
			+ path + "/";
%>
<!DOCTYPE html>
<html lang="zh-CN">

<head>
    <base href="<%=basePath%>">
    <meta charset="UTF-8">
    <%@ include file="../top.jsp"%>
    <script type="text/javascript" src="//code.jquery.com/jquery-2.0.3.min.js"></script>
    <link rel="stylesheet" href="vendors/jquery-confirm/jquery-confirm.min.css" media="screen">
</head>

<body>
    <%@ include file="../nav.jsp"%>

    <div class="news-container">
        <div class="row">
            <h1 class="home-title">Admin Operation Logs</h1>
            <hr style="border:0;background-color:#d4d4d4;height:1px;" />
        </div>
    </div>

    <div class="news-container">
        <div class="row">
            <div class="span12">
                <form class="form-horizontal">
                    <fieldset>
                        <div class="panel panel-default">
                            <div class="panel-heading">
                                <div class="text-muted bootstrap-admin-box-title"><strong>All operation records</strong></div>
                            </div>
                            <div class="bootstrap-admin-panel-content">
                                <div class="table-responsive">
                                    <table class="table table-striped table-hover" style="table-layout:fixed;word-break:break-all">
                                        <thead>
                                            <tr>
                                                <th>Operator</th>
                                                <th>IP</th>
                                                <th>Time</th>
                                                <th>Operation Detail</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <c:forEach items="${ ops }" var="op">
                                            <tr>
                                            	<td><a class="text-muted" style="text-decoration: none;" href="admin/edituser/${ op.operatorid }">${ op.name }</a></td>
                                                <td>${ op.ipaddr }</td>
                                                <td><fmt:formatDate value="${ op.operatetime }" pattern="yyyy-MM-dd HH:mm:ss" /></td>
                                                <td>${ op.operatefunc }</td>
                                            </tr>
                                        	</c:forEach>
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                        </div>        
                    </fieldset>
                </form>
            </div>
        </div>
    </div>
    <br/>


    <br/>

    <%@ include file="footer-admin.jsp"%>
    <script type="text/javascript" src="vendors/jquery-confirm/jquery-confirm.min.js"></script>
</body>

</html>