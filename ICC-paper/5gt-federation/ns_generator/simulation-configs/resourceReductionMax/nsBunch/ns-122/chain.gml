graph [
  node [
    id 0
    label 1
    disk 7
    cpu 3
    memory 7
  ]
  node [
    id 1
    label 2
    disk 5
    cpu 1
    memory 8
  ]
  node [
    id 2
    label 3
    disk 9
    cpu 1
    memory 10
  ]
  node [
    id 3
    label 4
    disk 3
    cpu 4
    memory 6
  ]
  node [
    id 4
    label 5
    disk 4
    cpu 1
    memory 16
  ]
  node [
    id 5
    label 6
    disk 5
    cpu 1
    memory 1
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 35
    bw 60
  ]
  edge [
    source 0
    target 1
    delay 29
    bw 122
  ]
  edge [
    source 1
    target 2
    delay 30
    bw 72
  ]
  edge [
    source 1
    target 3
    delay 25
    bw 74
  ]
  edge [
    source 1
    target 4
    delay 27
    bw 192
  ]
  edge [
    source 2
    target 5
    delay 25
    bw 125
  ]
  edge [
    source 3
    target 5
    delay 33
    bw 184
  ]
  edge [
    source 4
    target 5
    delay 29
    bw 98
  ]
]
