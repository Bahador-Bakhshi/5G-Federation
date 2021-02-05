graph [
  node [
    id 0
    label 1
    disk 7
    cpu 1
    memory 14
  ]
  node [
    id 1
    label 2
    disk 9
    cpu 1
    memory 7
  ]
  node [
    id 2
    label 3
    disk 10
    cpu 3
    memory 7
  ]
  node [
    id 3
    label 4
    disk 9
    cpu 1
    memory 2
  ]
  node [
    id 4
    label 5
    disk 8
    cpu 2
    memory 6
  ]
  node [
    id 5
    label 6
    disk 2
    cpu 3
    memory 6
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 34
    bw 175
  ]
  edge [
    source 0
    target 1
    delay 31
    bw 55
  ]
  edge [
    source 1
    target 2
    delay 29
    bw 57
  ]
  edge [
    source 2
    target 3
    delay 28
    bw 111
  ]
  edge [
    source 2
    target 4
    delay 30
    bw 88
  ]
  edge [
    source 3
    target 5
    delay 31
    bw 142
  ]
  edge [
    source 4
    target 5
    delay 35
    bw 185
  ]
]
