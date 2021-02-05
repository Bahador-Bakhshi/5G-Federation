graph [
  node [
    id 0
    label 1
    disk 10
    cpu 4
    memory 12
  ]
  node [
    id 1
    label 2
    disk 5
    cpu 2
    memory 10
  ]
  node [
    id 2
    label 3
    disk 2
    cpu 3
    memory 8
  ]
  node [
    id 3
    label 4
    disk 9
    cpu 1
    memory 5
  ]
  node [
    id 4
    label 5
    disk 3
    cpu 3
    memory 13
  ]
  node [
    id 5
    label 6
    disk 6
    cpu 2
    memory 7
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 33
    bw 153
  ]
  edge [
    source 0
    target 1
    delay 27
    bw 187
  ]
  edge [
    source 1
    target 2
    delay 26
    bw 175
  ]
  edge [
    source 2
    target 3
    delay 34
    bw 79
  ]
  edge [
    source 2
    target 4
    delay 31
    bw 135
  ]
  edge [
    source 2
    target 5
    delay 31
    bw 101
  ]
]
