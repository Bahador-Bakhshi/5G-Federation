graph [
  node [
    id 0
    label 1
    disk 9
    cpu 3
    memory 8
  ]
  node [
    id 1
    label 2
    disk 8
    cpu 2
    memory 15
  ]
  node [
    id 2
    label 3
    disk 9
    cpu 4
    memory 2
  ]
  node [
    id 3
    label 4
    disk 3
    cpu 1
    memory 13
  ]
  node [
    id 4
    label 5
    disk 4
    cpu 1
    memory 9
  ]
  node [
    id 5
    label 6
    disk 9
    cpu 2
    memory 6
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 27
    bw 181
  ]
  edge [
    source 0
    target 1
    delay 34
    bw 126
  ]
  edge [
    source 1
    target 2
    delay 31
    bw 149
  ]
  edge [
    source 1
    target 3
    delay 25
    bw 158
  ]
  edge [
    source 1
    target 4
    delay 31
    bw 179
  ]
  edge [
    source 2
    target 5
    delay 33
    bw 130
  ]
  edge [
    source 3
    target 5
    delay 31
    bw 158
  ]
  edge [
    source 4
    target 5
    delay 32
    bw 125
  ]
]
