graph [
  node [
    id 0
    label 1
    disk 5
    cpu 4
    memory 1
  ]
  node [
    id 1
    label 2
    disk 5
    cpu 3
    memory 14
  ]
  node [
    id 2
    label 3
    disk 1
    cpu 2
    memory 13
  ]
  node [
    id 3
    label 4
    disk 10
    cpu 4
    memory 14
  ]
  node [
    id 4
    label 5
    disk 1
    cpu 2
    memory 5
  ]
  node [
    id 5
    label 6
    disk 4
    cpu 4
    memory 12
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 25
    bw 149
  ]
  edge [
    source 0
    target 1
    delay 29
    bw 121
  ]
  edge [
    source 0
    target 2
    delay 28
    bw 120
  ]
  edge [
    source 0
    target 3
    delay 31
    bw 171
  ]
  edge [
    source 1
    target 4
    delay 35
    bw 114
  ]
  edge [
    source 2
    target 5
    delay 27
    bw 163
  ]
]
