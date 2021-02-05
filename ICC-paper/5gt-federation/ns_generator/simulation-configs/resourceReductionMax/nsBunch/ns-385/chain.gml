graph [
  node [
    id 0
    label 1
    disk 3
    cpu 3
    memory 15
  ]
  node [
    id 1
    label 2
    disk 1
    cpu 2
    memory 13
  ]
  node [
    id 2
    label 3
    disk 6
    cpu 4
    memory 7
  ]
  node [
    id 3
    label 4
    disk 3
    cpu 3
    memory 4
  ]
  node [
    id 4
    label 5
    disk 4
    cpu 3
    memory 2
  ]
  node [
    id 5
    label 6
    disk 6
    cpu 4
    memory 11
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 31
    bw 174
  ]
  edge [
    source 0
    target 1
    delay 28
    bw 167
  ]
  edge [
    source 0
    target 2
    delay 33
    bw 56
  ]
  edge [
    source 1
    target 3
    delay 35
    bw 137
  ]
  edge [
    source 2
    target 3
    delay 25
    bw 142
  ]
  edge [
    source 3
    target 4
    delay 35
    bw 148
  ]
  edge [
    source 4
    target 5
    delay 29
    bw 91
  ]
]
