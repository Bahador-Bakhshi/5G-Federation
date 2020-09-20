graph [
  node [
    id 0
    label 1
    disk 9
    cpu 2
    memory 15
  ]
  node [
    id 1
    label 2
    disk 6
    cpu 1
    memory 9
  ]
  node [
    id 2
    label 3
    disk 7
    cpu 2
    memory 10
  ]
  node [
    id 3
    label 4
    disk 9
    cpu 2
    memory 15
  ]
  node [
    id 4
    label 5
    disk 1
    cpu 3
    memory 14
  ]
  node [
    id 5
    label 6
    disk 3
    cpu 2
    memory 3
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 33
    bw 100
  ]
  edge [
    source 0
    target 1
    delay 26
    bw 60
  ]
  edge [
    source 1
    target 2
    delay 35
    bw 139
  ]
  edge [
    source 2
    target 3
    delay 26
    bw 52
  ]
  edge [
    source 3
    target 4
    delay 26
    bw 108
  ]
  edge [
    source 3
    target 5
    delay 30
    bw 72
  ]
]
