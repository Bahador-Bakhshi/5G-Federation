graph [
  node [
    id 0
    label 1
    disk 3
    cpu 1
    memory 1
  ]
  node [
    id 1
    label 2
    disk 10
    cpu 4
    memory 16
  ]
  node [
    id 2
    label 3
    disk 10
    cpu 2
    memory 5
  ]
  node [
    id 3
    label 4
    disk 10
    cpu 4
    memory 6
  ]
  node [
    id 4
    label 5
    disk 10
    cpu 4
    memory 1
  ]
  node [
    id 5
    label 6
    disk 3
    cpu 1
    memory 15
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 30
    bw 129
  ]
  edge [
    source 0
    target 1
    delay 30
    bw 53
  ]
  edge [
    source 0
    target 2
    delay 33
    bw 127
  ]
  edge [
    source 1
    target 3
    delay 28
    bw 193
  ]
  edge [
    source 2
    target 4
    delay 27
    bw 151
  ]
  edge [
    source 3
    target 4
    delay 29
    bw 199
  ]
  edge [
    source 4
    target 5
    delay 31
    bw 135
  ]
]
