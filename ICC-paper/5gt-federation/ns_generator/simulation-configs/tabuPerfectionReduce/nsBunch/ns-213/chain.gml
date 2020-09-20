graph [
  node [
    id 0
    label 1
    disk 5
    cpu 1
    memory 10
  ]
  node [
    id 1
    label 2
    disk 9
    cpu 1
    memory 6
  ]
  node [
    id 2
    label 3
    disk 2
    cpu 3
    memory 15
  ]
  node [
    id 3
    label 4
    disk 8
    cpu 4
    memory 14
  ]
  node [
    id 4
    label 5
    disk 4
    cpu 4
    memory 13
  ]
  node [
    id 5
    label 6
    disk 3
    cpu 3
    memory 16
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 27
    bw 198
  ]
  edge [
    source 0
    target 1
    delay 27
    bw 96
  ]
  edge [
    source 0
    target 2
    delay 31
    bw 152
  ]
  edge [
    source 0
    target 3
    delay 27
    bw 173
  ]
  edge [
    source 1
    target 5
    delay 31
    bw 75
  ]
  edge [
    source 2
    target 4
    delay 33
    bw 153
  ]
  edge [
    source 3
    target 5
    delay 35
    bw 183
  ]
  edge [
    source 4
    target 5
    delay 28
    bw 157
  ]
]
